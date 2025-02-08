import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Menu
from tkinterdnd2 import DND_FILES, TkinterDnD
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
import os
from PIL import Image, ImageTk

class AutocompletePanel:
    def __init__(self, parent, label_text, is_spell_panel=False):
        self.frame = ttk.Frame(parent)
        self.values = {'names': [], 'ids': []}  # Split values into names and IDs for spell panel
        self.is_spell_panel = is_spell_panel
        ttk.Label(self.frame, text=label_text).pack(side=tk.TOP, anchor=tk.W)
        entry_frame = ttk.Frame(self.frame)
        entry_frame.pack(fill=tk.X)
        self.entry = ttk.Entry(entry_frame)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.clear_btn = ttk.Button(entry_frame, text="×", width=2, command=self.clear)
        self.clear_btn.pack(side=tk.RIGHT)
        self.listbox = tk.Listbox(self.frame, height=5, exportselection=False)
        self.listbox.pack(fill=tk.X)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.entry.bind('<KeyRelease>', self.update_suggestions)

    def clear(self):
        self.entry.delete(0, tk.END)
        self.listbox.delete(0, tk.END)

    def update_suggestions(self, event=None):
        search_term = self.entry.get().lower()
        self.listbox.delete(0, tk.END)
        
        if not self.is_spell_panel:
            # Regular panel behavior for non-spell panels
            for value in self.values:
                if search_term in str(value).lower():
                    self.listbox.insert(tk.END, value)
        else:
            # Special handling for spell panel
            is_numeric = search_term.isdigit()
            if is_numeric:
                # Search in spell IDs
                search_int = int(search_term)
                for value in self.values['ids']:
                    if search_term in str(value):
                        # Show both ID and name in the suggestion
                        name_index = list(self.values['ids']).index(value)
                        spell_name = self.values['names'][name_index] if name_index < len(self.values['names']) else ""
                        display_text = f"{value} - {spell_name}"
                        self.listbox.insert(tk.END, str(value))
            else:
                # Search in spell names
                for value in self.values['names']:
                    if search_term in str(value).lower():
                        # Show both name and ID in the suggestion
                        id_index = list(self.values['names']).index(value)
                        spell_id = self.values['ids'][id_index] if id_index < len(self.values['ids']) else ""
                        display_text = f"{value} - {spell_id}"
                        self.listbox.insert(tk.END, value)

    def on_select(self, event):
        if self.listbox.curselection():
            selected = self.listbox.get(self.listbox.curselection())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, selected)

    def set_values(self, values):
        if self.is_spell_panel:
            if isinstance(values, dict):
                self.values = values
            else:
                # If given a single list, assume they're all names
                self.values = {'names': values, 'ids': []}
        else:
            # For non-spell panels, maintain backwards compatibility
            if isinstance(values, list):
                self.values = values
            else:
                self.values = []

class CSVVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Combat Data Visualizer")
        self.root.geometry("1000x800")
        self.df = None
        self.plot_window = None
        self.current_event_type = None
        self.map_image = None  # Store the map image
        self.last_plot_params = None  # Store last plot parameters

        self.event_groups = {
            'Deaths': ['UNIT_DIED'],
            'Damage/Heals': [
                'RANGE_DAMAGE','SPELL_HEAL','SPELL_PERIODIC_HEAL',
                'SPELL_PERIODIC_DAMAGE','SPELL_DAMAGE','SWING_DAMAGE_LANDED'
            ],
            'Casting': ['SPELL_CAST_SUCCESS','SWING_DAMAGE'],
            'Movement': ['MOVEMENT_TRACKER', 'SPELL_CAST_SUCCESS', 'SWING_DAMAGE',
                        'RANGE_DAMAGE','SPELL_HEAL','SPELL_PERIODIC_HEAL',
                        'SPELL_PERIODIC_DAMAGE','SPELL_DAMAGE','SWING_DAMAGE_LANDED']
        }

        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add image upload frame
        image_frame = ttk.LabelFrame(main_frame, text="Map Image")
        image_frame.pack(fill=tk.X, pady=5)
        
        # Create a frame for the image preview
        self.preview_frame = ttk.Frame(image_frame, width=200, height=150)
        self.preview_frame.pack(side=tk.LEFT, padx=5, pady=5)
        self.preview_frame.pack_propagate(False)  # Prevent frame from shrinking
        
        # Add image preview label
        self.preview_label = ttk.Label(self.preview_frame, text="Drag & Drop\nMap Image Here")
        self.preview_label.pack(expand=True)
        
        # Make the preview frame a drop target
        self.preview_frame.drop_target_register(DND_FILES)
        self.preview_frame.dnd_bind('<<Drop>>', self.handle_image_drop)
        
        # Add button frame
        image_btn_frame = ttk.Frame(image_frame)
        image_btn_frame.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Add select image button
        ttk.Button(image_btn_frame, text="Select Image", 
                  command=self.select_image).pack(pady=2)
        
        # Add clear image button
        ttk.Button(image_btn_frame, text="Clear Image", 
                  command=self.clear_image).pack(pady=2)
        
        # Add save/load settings buttons
        ttk.Button(image_btn_frame, text="Save Settings", 
                  command=self.save_map_settings).pack(pady=2)
        ttk.Button(image_btn_frame, text="Load Settings", 
                  command=self.load_map_settings).pack(pady=2)
        
        # Add Load CSV button
        ttk.Button(image_btn_frame, text="Load CSV",
                  command=self.load_csv).pack(pady=2)

        # Add boss position frame
        boss_frame = ttk.Frame(image_frame)
        boss_frame.pack(side=tk.LEFT, padx=5)
        ttk.Label(boss_frame, text="Boss Position:").pack()
        
        boss_coord_frame = ttk.Frame(boss_frame)
        boss_coord_frame.pack()
        
        ttk.Label(boss_coord_frame, text="X:").pack(side=tk.LEFT)
        self.boss_x = ttk.Entry(boss_coord_frame, width=10)
        self.boss_x.pack(side=tk.LEFT, padx=2)
        
        ttk.Label(boss_coord_frame, text="Y:").pack(side=tk.LEFT)
        self.boss_y = ttk.Entry(boss_coord_frame, width=10)
        self.boss_y.pack(side=tk.LEFT, padx=2)

        # Add map control frame
        map_control_frame = ttk.LabelFrame(image_frame, text="Map Controls")
        map_control_frame.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        
        # Add reference data button
        ttk.Button(map_control_frame, text="Plot Reference Data",
                  command=self.plot_reference_data).pack(pady=2)
        
        # Map scale
        ttk.Label(map_control_frame, text="Map Scale:").pack()
        self.map_scale_var = tk.StringVar(value="1.0")
        ttk.Entry(map_control_frame, textvariable=self.map_scale_var, width=10).pack()
        
        # Map rotation
        ttk.Label(map_control_frame, text="Map Rotation:").pack()
        self.map_rotation_var = tk.StringVar(value="0")
        ttk.Entry(map_control_frame, textvariable=self.map_rotation_var, width=10).pack()
        
        # Map offset
        offset_frame = ttk.Frame(map_control_frame)
        offset_frame.pack(pady=2)
        ttk.Label(offset_frame, text="Map Offset X:").pack(side=tk.LEFT)
        self.map_offset_x = ttk.Entry(offset_frame, width=10)
        self.map_offset_x.pack(side=tk.LEFT, padx=2)
        self.map_offset_x.insert(0, "0")
        
        offset_frame2 = ttk.Frame(map_control_frame)
        offset_frame2.pack(pady=2)
        ttk.Label(offset_frame2, text="Map Offset Y:").pack(side=tk.LEFT)
        self.map_offset_y = ttk.Entry(offset_frame2, width=10)
        self.map_offset_y.pack(side=tk.LEFT, padx=2)
        self.map_offset_y.insert(0, "0")

        # Data control frame
        data_control_frame = ttk.LabelFrame(image_frame, text="Data Controls")
        data_control_frame.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        
        # Data scale
        ttk.Label(data_control_frame, text="Data Scale:").pack()
        self.data_scale_var = tk.StringVar(value="1.0")
        ttk.Entry(data_control_frame, textvariable=self.data_scale_var, width=10).pack()
        
        # Data rotation
        ttk.Label(data_control_frame, text="Data Rotation:").pack()
        self.data_rotation_var = tk.StringVar(value="0")
        ttk.Entry(data_control_frame, textvariable=self.data_rotation_var, width=10).pack()

        # Add debug log frame
        log_frame = ttk.LabelFrame(main_frame, text="Filter Log")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Add text widget for debug logs
        self.log_text = tk.Text(log_frame, height=8, wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add scrollbar for log text
        log_scrollbar = ttk.Scrollbar(self.log_text, orient="vertical", command=self.log_text.yview)
        log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)
        
        # Make log text read-only
        self.log_text.configure(state='disabled')

        # Add clear log button
        clear_log_btn = ttk.Button(log_frame, text="Clear Log", command=self.clear_log)
        clear_log_btn.pack(pady=2)

        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=5)
        ttk.Label(control_frame, text="Event Type:").pack(side=tk.LEFT)

        for group_name in self.event_groups:
            btn = ttk.Button(control_frame, text=group_name,
                             command=lambda gn=group_name: self.set_event_type(gn))
            btn.pack(side=tk.LEFT, padx=2)

        self.aura_menubtn = ttk.Menubutton(control_frame, text="Auras")
        aura_menu = Menu(self.aura_menubtn, tearoff=0)
        aura_menu.add_command(
            label="Applied + Refreshed",
            command=lambda: self.set_event_type(['SPELL_AURA_APPLIED', 'SPELL_AURA_REFRESH'], True, "Applied + Refreshed")
        )
        aura_menu.add_command(
            label="Removed",
            command=lambda: self.set_event_type(['SPELL_AURA_REMOVED'], True, "Removed")
        )
        aura_menu.add_command(
            label="Applied",
            command=lambda: self.set_event_type(['SPELL_AURA_APPLIED'], True, "Applied")
        )
        aura_menu.add_command(
            label="Refreshed",
            command=lambda: self.set_event_type(['SPELL_AURA_REFRESH'], True, "Refreshed")
        )
        self.aura_menubtn['menu'] = aura_menu
        self.aura_menubtn.pack(side=tk.LEFT, padx=2)

        filter_frame = ttk.Frame(main_frame)
        filter_frame.pack(fill=tk.X, pady=10)

        self.unit_panel = AutocompletePanel(filter_frame, "Unit Filter")
        self.unit_panel.frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        self.spell_panel = AutocompletePanel(filter_frame, "Spell Filter: Name or ID", is_spell_panel=True)
        self.spell_panel.frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        encounter_frame = ttk.Frame(filter_frame)
        encounter_frame.pack(side=tk.LEFT, padx=5)
        ttk.Label(encounter_frame, text="Encounter ID:").pack()
        self.encounter_entry = ttk.Entry(encounter_frame, width=10)
        self.encounter_entry.pack()
        
        # Add auto-fill button for encounter IDs
        def autofill_encounters():
            if self.df is not None:
                encounter_ids = sorted(self.df['encounter id'].unique())
                self.encounter_entry.delete(0, tk.END)
                self.encounter_entry.insert(0, ','.join(map(str, encounter_ids)))
        
        ttk.Button(encounter_frame, text="Auto-fill IDs", command=autofill_encounters).pack()

        threshold_frame = ttk.Frame(filter_frame)
        threshold_frame.pack(side=tk.LEFT, padx=5)
        ttk.Label(threshold_frame, text="Death Threshold:").pack()
        self.death_threshold = ttk.Entry(threshold_frame, width=5)
        self.death_threshold.pack()

        # Add timeframe filter entries
        timeframe_frame = ttk.Frame(filter_frame)
        timeframe_frame.pack(side=tk.LEFT, padx=5)
        ttk.Label(timeframe_frame, text="Start Time (s):").pack()
        self.start_time_entry = ttk.Entry(timeframe_frame, width=10)
        self.start_time_entry.pack()
        ttk.Label(timeframe_frame, text="End Time (s):").pack()
        self.end_time_entry = ttk.Entry(timeframe_frame, width=10)
        self.end_time_entry.pack()

        btn_frame = ttk.Frame(filter_frame)
        btn_frame.pack(side=tk.LEFT, padx=10)
        ttk.Button(btn_frame, text="Scatter", command=lambda: self.plot_data('scatter')).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="Heatmap", command=lambda: self.plot_data('heatmap')).pack(side=tk.LEFT)
        ttk.Button(btn_frame, text="Average Movement", command=self.prompt_average_movement).pack(side=tk.LEFT)

        self.status = ttk.Label(main_frame, text="Ready")
        self.status.pack(fill=tk.X, pady=5)

        root.drop_target_register(DND_FILES)
        root.dnd_bind('<<Drop>>', self.handle_file_drop)

    def set_event_type(self, group_name, is_aura_suboption=False, label=None):
        if is_aura_suboption:
            self.current_event_type = group_name
            self.status.config(text=f"Showing: Auras - {label}")
        else:
            self.current_event_type = self.event_groups[group_name]
            self.status.config(text=f"Showing: {group_name}")

        # Clear any existing filters
        self.unit_panel.clear()
        self.spell_panel.clear()
        self.encounter_entry.delete(0, tk.END)
        self.death_threshold.delete(0, tk.END)
        self.start_time_entry.delete(0, tk.END)
        self.end_time_entry.delete(0, tk.END)

        # If this is an aura event, update the log
        if is_aura_suboption:
            self.log_message(f"\nSelected Aura Events: {', '.join(group_name)}")
            self.log_message(f"Type: {label}")

        self.aura_menubtn = ttk.Menubutton(control_frame, text="Auras")
        aura_menu = Menu(self.aura_menubtn, tearoff=0)
        aura_menu.add_command(
            label="Applied + Refreshed",
            command=lambda: self.set_event_type(['SPELL_AURA_APPLIED', 'SPELL_AURA_REFRESH'], True, "Applied + Refreshed")
        )
        aura_menu.add_command(
            label="Removed",
            command=lambda: self.set_event_type(['SPELL_AURA_REMOVED'], True, "Removed")
        )
        aura_menu.add_command(
            label="Applied",
            command=lambda: self.set_event_type(['SPELL_AURA_APPLIED'], True, "Applied")
        )
        aura_menu.add_command(
            label="Refreshed",
            command=lambda: self.set_event_type(['SPELL_AURA_REFRESH'], True, "Refreshed")
        )
        self.aura_menubtn['menu'] = aura_menu
        self.aura_menubtn.pack(side=tk.LEFT, padx=2)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if path:
            self.process_file(path)

    def handle_file_drop(self, event):
        path = event.data.strip('{}"')
        if path.lower().endswith('.csv'):
            self.process_file(path)
        else:
            messagebox.showwarning("Invalid File", "Please drop a CSV file")

    def log_message(self, message):
        """Add a message to both the terminal and the log window"""
        print(message)
        self.log_text.configure(state='normal')
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)  # Scroll to the bottom
        self.log_text.configure(state='disabled')

    def clear_log(self):
        """Clear the log window"""
        self.log_text.configure(state='normal')
        self.log_text.delete(1.0, tk.END)
        self.log_text.configure(state='disabled')

    def process_file(self, path):
        try:
            self.df = pd.read_csv(path)
            self.df['timestamp'] = pd.to_datetime(
                self.df['timestamp'], format="%m/%d/%Y %H:%M:%S.%f", errors='coerce'
            )
            # Convert spell_id to integer, handling NaN values
            self.df['spell id'] = pd.to_numeric(self.df['spell id'], errors='coerce').fillna(-1).astype('Int64')
            
            units = sorted(set(self.df['Damage source'].dropna()) | set(self.df['Spell destination'].dropna()))
            
            # Process spell names and IDs
            spell_names = sorted(self.df['spell name'].dropna().unique())
            spell_ids = sorted(self.df['spell id'].dropna().astype('Int64').unique())
            spell_values = {
                'names': spell_names,
                'ids': spell_ids
            }
            
            self.unit_panel.set_values(units)
            self.spell_panel.set_values(spell_values)
            self.log_message(f"Loaded {len(self.df)} records")
            self.log_message(f"Unique spell names: {len(spell_names)}")
            self.log_message(f"Unique spell IDs: {len(spell_ids)}")
            messagebox.showinfo("Loaded", f"Successfully loaded {len(self.df)} records")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{str(e)}")

    def plot_data(self, plot_type):
        if self.df is None or not self.current_event_type:
            messagebox.showwarning("Error", "Please load data and select event type first")
            return

        try:
            if 'MOVEMENT_TRACKER' in self.current_event_type:
                self.plot_movement()
                return

            filtered = self.df.copy()
            self.log_message("\nFiltering Data:")
            self.log_message(f"Initial records: {len(filtered)}")
            
            encounter_ids = []
            if self.encounter_entry.get():
                try:
                    encounter_ids = [int(x.strip()) for x in self.encounter_entry.get().split(',')]
                    filtered = filtered[filtered['encounter id'].isin(encounter_ids)]
                    self.log_message(f"After encounter filter: {len(filtered)} records")
                    if filtered.empty:
                        raise ValueError(f"No data for encounters {encounter_ids}")
                except ValueError:
                    messagebox.showwarning("Invalid Input", "Please enter comma-separated numeric encounter IDs")
                    return

            # Apply death threshold filtering for all encounters
            if self.death_threshold.get():
                try:
                    threshold = int(self.death_threshold.get())
                    # Get all unique encounter IDs if none specified
                    if not encounter_ids:
                        encounter_ids = filtered['encounter id'].unique()
                    
                    # Create a mask for valid events (before death threshold)
                    valid_events_mask = pd.Series(False, index=filtered.index)
                    
                    for enc_id in encounter_ids:
                        enc_data = filtered[filtered['encounter id'] == enc_id]
                        deaths = enc_data[enc_data['event type'] == 'UNIT_DIED']
                        
                        if not deaths.empty and len(deaths) >= threshold:
                            # Get the timestamp of the nth death
                            cutoff = deaths.iloc[threshold-1]['timestamp']
                            # Include all events in this encounter up to the cutoff
                            valid_events_mask |= (
                                (filtered['encounter id'] == enc_id) & 
                                (filtered['timestamp'] <= cutoff)
                            )
                        else:
                            # If encounter has fewer deaths than threshold, include all its events
                            valid_events_mask |= (filtered['encounter id'] == enc_id)
                    
                    filtered = filtered[valid_events_mask]
                    self.log_message(f"After death threshold: {len(filtered)} records")
                except ValueError as e:
                    messagebox.showwarning("Threshold Error", str(e))
                    return

            # Apply timeframe filter
            start_time = self.start_time_entry.get()
            end_time = self.end_time_entry.get()
            if start_time or end_time:
                try:
                    if start_time:
                        start_time = float(start_time)
                        filtered = filtered[filtered['relative fight time (s)'] >= start_time]
                    if end_time:
                        end_time = float(end_time)
                        filtered = filtered[filtered['relative fight time (s)'] <= end_time]
                    self.log_message(f"After timeframe filter: {len(filtered)} records")
                except ValueError:
                    messagebox.showwarning("Invalid Input", "Please enter valid numeric values for start and end times")
                    return

            filtered = filtered[filtered['event type'].isin(self.current_event_type)]
            self.log_message(f"After event type filter: {len(filtered)} records")
            
            unit = self.unit_panel.entry.get()
            if unit:
                filtered = filtered[
                    (filtered['Damage source'] == unit) | (filtered['Spell destination'] == unit)
                ]
                self.log_message(f"After unit filter: {len(filtered)} records")
            
            spell_filter = self.spell_panel.entry.get()
            if spell_filter:
                if spell_filter.isdigit():
                    # Filter by spell ID (convert to integer for comparison)
                    spell_id = int(spell_filter)
                    filtered = filtered[filtered['spell id'] == spell_id]
                    self.log_message(f"After spell ID filter ({spell_id}): {len(filtered)} records")
                else:
                    # Filter by spell name
                    filtered = filtered[filtered['spell name'] == spell_filter]
                    self.log_message(f"After spell name filter ({spell_filter}): {len(filtered)} records")
                    
            if filtered.empty:
                raise ValueError("No data matches filters")

            # Store the current plot parameters
            self.last_plot_params = {
                'plot_type': plot_type,
                'filtered_data': filtered.copy(),
                'encounter_ids': encounter_ids,
                'data_scale': float(self.data_scale_var.get()),
                'data_rotation': float(self.data_rotation_var.get())
            }

            if self.plot_window:
                self.plot_window.destroy()
            self.plot_window = tk.Toplevel(self.root)
            self.plot_window.title("Combat Visualization")

            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)

            # Plot the map if available
            if self.map_image is not None:
                try:
                    img = np.array(self.map_image)
                    h_orig, w_orig, *_ = img.shape
                    
                    map_scale = float(self.map_scale_var.get())
                    map_rotation = float(self.map_rotation_var.get())
                    map_offset_x = float(self.map_offset_x.get())
                    map_offset_y = float(self.map_offset_y.get())
                    
                    pil_img = Image.fromarray(img)
                    if map_rotation != 0:
                        pil_img = pil_img.rotate(map_rotation, expand=True, resample=Image.BICUBIC)
                    
                    map_w = int(w_orig * map_scale)
                    map_h = int(h_orig * map_scale)
                    pil_img = pil_img.resize((map_w, map_h), Image.LANCZOS)
                    img_small = np.array(pil_img)
                    
                    ax.imshow(img_small, extent=[map_offset_x, map_offset_x + map_w, 
                                               map_offset_y + map_h, map_offset_y],
                             alpha=0.5, zorder=1)
                except Exception as e:
                    print(f"Error displaying map: {e}")

            # Get data transformation parameters
            data_scale = float(self.data_scale_var.get())
            data_rotation = float(self.data_rotation_var.get())

            # Plot boss position if coordinates are provided
            if self.boss_x.get() and self.boss_y.get():
                try:
                    bx = float(self.boss_x.get())
                    by = float(self.boss_y.get())
                    ax.scatter(bx, by, s=200, marker='*',
                             color='gold', edgecolor='black',
                             zorder=10, label='Boss Position')
                except ValueError:
                    pass

            # Plot the data points
            if plot_type == 'scatter' and not self.unit_panel.entry.get():
                # Get unique destination units for color mapping
                dest_units = filtered['Spell destination'].unique()
                colors = self.get_color_palette(len(dest_units))
                color_map = {unit: colors[i] for i, unit in enumerate(dest_units)}
                
                x_coords = pd.to_numeric(filtered['X coord'], errors='coerce')
                y_coords = pd.to_numeric(filtered['Y coord'], errors='coerce')
                valid = x_coords.notna() & y_coords.notna()
                
                # Create scatter plots by source
                scatter_artists = []
                for unit in dest_units:
                    unit_mask = filtered['Spell destination'] == unit
                    unit_data = filtered[unit_mask & valid].copy()
                    if not unit_data.empty:
                        scatter = ax.scatter(
                            unit_data['X coord'].astype(float),
                            unit_data['Y coord'].astype(float),
                            color=color_map[unit],
                            alpha=0.8,
                            label=unit,
                            picker=True,
                            zorder=5
                        )
                        scatter_artists.append(scatter)
                        
                        # Store data for tooltips
                        scatter.unit_data = unit_data.reset_index(drop=True)  # Reset index for proper lookup
                        scatter.x_coords = unit_data['X coord'].astype(float).values
                        scatter.y_coords = unit_data['Y coord'].astype(float).values

                # Create legend with draggable and clickable functionality
                ax.legend()
                leg = ax.get_legend()
                if leg and scatter_artists:
                    leg.set_draggable(True)
                    legend_map = {}
                    for handle, scatter in zip(leg.legend_handles, scatter_artists):
                        handle.set_picker(5)  # Set picker tolerance
                        legend_map[handle] = scatter

                    def on_pick(event):
                        if event.artist in legend_map:
                            scatter = legend_map[event.artist]
                            visible = not scatter.get_visible()
                            scatter.set_visible(visible)
                            event.artist.set_alpha(1.0 if visible else 0.6)
                            fig.canvas.draw_idle()

                    fig.canvas.mpl_connect('pick_event', on_pick)

                # Create tooltip
                tooltip = ax.annotate("",
                    xy=(0, 0), xytext=(10, 10),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9),
                    visible=False
                )

                def on_motion(event):
                    if event.inaxes == ax:
                        for scatter in scatter_artists:
                            if scatter.get_visible():
                                cont, ind = scatter.contains(event)
                                if cont:
                                    # Get data point info
                                    point_idx = ind["ind"][0]
                                    unit_data = scatter.unit_data.iloc[point_idx]
                                    
                                    # Format tooltip text
                                    tooltip_text = f"Unit: {unit_data['Spell destination']}\n"
                                    tooltip_text += f"Event: {unit_data['event type']}\n"
                                    if not pd.isna(unit_data['spell name']):
                                        tooltip_text += f"Spell: {unit_data['spell name']}\n"
                                    tooltip_text += f"Encounter: {unit_data['encounter id']}\n"
                                    tooltip_text += f"Time: {unit_data['relative fight time (s)']:.1f}s"
                                    if not pd.isna(unit_data['unit died sequence']):
                                        tooltip_text += f"\nDeath Sequence: {int(unit_data['unit died sequence'])}"
                                    
                                    # Update tooltip
                                    tooltip.set_text(tooltip_text)
                                    tooltip.xy = (scatter.x_coords[point_idx], scatter.y_coords[point_idx])
                                    tooltip.set_visible(True)
                                    fig.canvas.draw_idle()
                                    return
                        
                        tooltip.set_visible(False)
                        fig.canvas.draw_idle()

                fig.canvas.mpl_connect('motion_notify_event', on_motion)
            elif plot_type == 'heatmap':
                if encounter_ids:
                    cmap = plt.get_cmap('tab10')
                    scatter_artists = []
                    for idx, enc_id in enumerate(encounter_ids):
                        enc_data = filtered[filtered['encounter id'] == enc_id]
                        x_coords = pd.to_numeric(enc_data['X coord'], errors='coerce')
                        y_coords = pd.to_numeric(enc_data['Y coord'], errors='coerce')
                        valid = x_coords.notna() & y_coords.notna()

                        plot = sns.kdeplot(
                            x=x_coords[valid],
                            y=y_coords[valid],
                            cmap="Reds",
                            fill=True,
                            ax=ax,
                            label=f'Enc {enc_id}',
                            alpha=0.3
                        )
                        scatter_artists.append(plot)
                else:
                    x_coords = pd.to_numeric(filtered['X coord'], errors='coerce')
                    y_coords = pd.to_numeric(filtered['Y coord'], errors='coerce')
                    valid = x_coords.notna() & y_coords.notna()
                    sns.kdeplot(
                        x=x_coords[valid],
                        y=y_coords[valid],
                        cmap="Reds",
                        fill=True,
                        ax=ax,
                        alpha=0.3
                    )
            else:
                # Original scatter plot code for when a unit is selected
                if encounter_ids:
                    cmap = plt.get_cmap('tab10')
                    scatter_artists = []
                    for idx, enc_id in enumerate(encounter_ids):
                        enc_data = filtered[filtered['encounter id'] == enc_id]
                        x_coords = pd.to_numeric(enc_data['X coord'], errors='coerce')
                        y_coords = pd.to_numeric(enc_data['Y coord'], errors='coerce')
                        valid = x_coords.notna() & y_coords.notna()

                        scatter = ax.scatter(
                            x_coords[valid],
                            y_coords[valid],
                            color=cmap(idx % 10),
                            alpha=0.5,
                            label=f'Enc {enc_id}'
                        )
                        scatter_artists.append(scatter)
                else:
                    x_coords = pd.to_numeric(filtered['X coord'], errors='coerce')
                    y_coords = pd.to_numeric(filtered['Y coord'], errors='coerce')
                    valid = x_coords.notna() & y_coords.notna()
                    ax.scatter(x_coords[valid], y_coords[valid], alpha=0.5)

            # Add map visibility toggle if map is loaded
            legend_frame = ttk.Frame(self.plot_window)
            legend_frame.pack(side=tk.RIGHT, fill=tk.Y)
            
            if self.map_image is not None:
                map_var = tk.BooleanVar(value=True)
                ttk.Checkbutton(legend_frame, text="Show Map",
                              variable=map_var,
                              command=lambda: self.toggle_map_visibility(ax, map_var.get())).pack(pady=5)

            canvas = FigureCanvasTkAgg(fig, self.plot_window)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, self.plot_window)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showwarning("Plot Error", str(e))

    def update_plot(self, fig, ax):
        """Update the plot with current transformation parameters"""
        try:
            ax.clear()  # Clear the axis
            
            # Update map transformation
            if self.map_image is not None:
                img = np.array(self.map_image)
                h_orig, w_orig, *_ = img.shape
                
                map_scale = float(self.map_scale_var.get())
                map_rotation = float(self.map_rotation_var.get())
                map_offset_x = float(self.map_offset_x.get())
                map_offset_y = float(self.map_offset_y.get())
                
                pil_img = Image.fromarray(img)
                if map_rotation != 0:
                    pil_img = pil_img.rotate(map_rotation, expand=True, resample=Image.BICUBIC)
                
                map_w = int(w_orig * map_scale)
                map_h = int(h_orig * map_scale)
                pil_img = pil_img.resize((map_w, map_h), Image.LANCZOS)
                img_small = np.array(pil_img)
                
                ax.imshow(img_small, extent=[map_offset_x, map_offset_x + map_w, 
                                           map_offset_y + map_h, map_offset_y],
                         alpha=0.5, zorder=1)
            
            # Redraw data points if we have last plot parameters
            if self.last_plot_params:
                filtered = self.last_plot_params['filtered_data']
                data_scale = self.last_plot_params['data_scale']
                data_rotation = self.last_plot_params['data_rotation']
                
                # Plot boss position if coordinates are provided
                if self.boss_x.get() and self.boss_y.get():
                    try:
                        bx = float(self.boss_x.get())
                        by = float(self.boss_y.get())
                        ax.scatter(bx, by, s=200, marker='*',
                                 color='gold', edgecolor='black',
                                 zorder=10, label='Boss Position')
                    except ValueError:
                        pass
                
                if self.last_plot_params['plot_type'] == 'scatter':
                    x_coords = pd.to_numeric(filtered['X coord'], errors='coerce')
                    y_coords = pd.to_numeric(filtered['Y coord'], errors='coerce')
                    valid = x_coords.notna() & y_coords.notna()
                    
                    ax.scatter(x_coords[valid], y_coords[valid], alpha=0.5, zorder=5)
            
            fig.canvas.draw_idle()
        except Exception as e:
            messagebox.showwarning("Update Error", str(e))

    def toggle_map_visibility(self, ax, show_map):
        """Toggle the visibility of the map overlay"""
        for img in ax.images:
            img.set_visible(show_map)
        ax.figure.canvas.draw_idle()

    def plot_movement(self):
        try:
            unit = self.unit_panel.entry.get()
            if not unit:
                raise ValueError("Please enter a unit name for movement tracking")

            filtered = self.df.copy()
            encounter_ids = []
            if self.encounter_entry.get():
                try:
                    encounter_ids = [int(x.strip()) for x in self.encounter_entry.get().split(',')]
                    filtered = filtered[filtered['encounter id'].isin(encounter_ids)]
                    if filtered.empty:
                        raise ValueError(f"No data for encounters {encounter_ids}")
                except ValueError:
                    messagebox.showwarning("Invalid Input", "Please enter comma-separated numeric encounter IDs")
                    return

            # Apply death threshold filtering if specified
            if self.death_threshold.get():
                try:
                    threshold = int(self.death_threshold.get())
                    # Get all unique encounter IDs if none specified
                    if not encounter_ids:
                        encounter_ids = filtered['encounter id'].unique()
                    
                    # Create a mask for valid events (before death threshold)
                    valid_events_mask = pd.Series(False, index=filtered.index)
                    
                    for enc_id in encounter_ids:
                        enc_data = filtered[filtered['encounter id'] == enc_id]
                        deaths = enc_data[enc_data['event type'] == 'UNIT_DIED']
                        
                        if not deaths.empty and len(deaths) >= threshold:
                            # Get the timestamp of the nth death
                            cutoff = deaths.iloc[threshold-1]['timestamp']
                            # Include all events in this encounter up to the cutoff
                            valid_events_mask |= (
                                (filtered['encounter id'] == enc_id) & 
                                (filtered['timestamp'] <= cutoff)
                            )
                        else:
                            # If encounter has fewer deaths than threshold, include all its events
                            valid_events_mask |= (filtered['encounter id'] == enc_id)
                    
                    filtered = filtered[valid_events_mask]
                    self.log_message(f"After death threshold: {len(filtered)} records")
                except ValueError as e:
                    messagebox.showwarning("Threshold Error", str(e))
                    return

            source_events = ['SPELL_CAST_SUCCESS','SWING_DAMAGE']
            dest_events = [
                'RANGE_DAMAGE','SPELL_HEAL','SPELL_PERIODIC_HEAL',
                'SPELL_PERIODIC_DAMAGE','SPELL_DAMAGE','SWING_DAMAGE_LANDED'
            ]
            source_mask = filtered['event type'].isin(source_events) & (filtered['Damage source'] == unit)
            source_df = filtered[source_mask].copy()
            source_df['x'] = pd.to_numeric(source_df['X coord'], errors='coerce')
            source_df['y'] = pd.to_numeric(source_df['Y coord'], errors='coerce')

            dest_mask = filtered['event type'].isin(dest_events) & (filtered['Spell destination'] == unit)
            dest_df = filtered[dest_mask].copy()
            dest_df['x'] = pd.to_numeric(dest_df['X coord'], errors='coerce')
            dest_df['y'] = pd.to_numeric(dest_df['Y coord'], errors='coerce')

            movement = pd.concat([source_df, dest_df]).sort_values('timestamp')
            movement = movement.dropna(subset=['x','y'])
            if movement.empty:
                raise ValueError(f"No movement data found for {unit}")

            if self.plot_window:
                self.plot_window.destroy()
            self.plot_window = tk.Toplevel(self.root)
            self.plot_window.title(f"Movement Path - {unit}")
            fig = Figure(figsize=(12, 8))
            ax = fig.add_subplot(111)

            # Plot the map if available
            if self.map_image is not None:
                try:
                    img = np.array(self.map_image)
                    h_orig, w_orig, *_ = img.shape
                    
                    map_scale = float(self.map_scale_var.get())
                    map_rotation = float(self.map_rotation_var.get())
                    map_offset_x = float(self.map_offset_x.get())
                    map_offset_y = float(self.map_offset_y.get())
                    
                    pil_img = Image.fromarray(img)
                    if map_rotation != 0:
                        pil_img = pil_img.rotate(map_rotation, expand=True, resample=Image.BICUBIC)
                    
                    map_w = int(w_orig * map_scale)
                    map_h = int(h_orig * map_scale)
                    pil_img = pil_img.resize((map_w, map_h), Image.LANCZOS)
                    img_small = np.array(pil_img)
                    
                    ax.imshow(img_small, extent=[map_offset_x, map_offset_x + map_w, 
                                               map_offset_y + map_h, map_offset_y],
                             alpha=0.5, zorder=1)
                except Exception as e:
                    print(f"Error displaying map: {e}")

            # Plot boss position if coordinates are provided
            if self.boss_x.get() and self.boss_y.get():
                try:
                    bx = float(self.boss_x.get())
                    by = float(self.boss_y.get())
                    ax.scatter(bx, by, s=200, marker='*',
                             color='gold', edgecolor='black',
                             zorder=10, label='Boss Position')
                except ValueError:
                    pass

            cmap = plt.get_cmap('tab10')
            if encounter_ids:
                line_artists = []
                scatter_artists = []
                for idx, enc_id in enumerate(encounter_ids):
                    enc_data = movement[movement['encounter id'] == enc_id]
                    color = cmap(idx % 10)
                    line, = ax.plot(enc_data['x'], enc_data['y'], color=color, alpha=0.5, label=f'Enc {enc_id}')
                    scatter = ax.scatter(enc_data['x'], enc_data['y'], color=color, alpha=0.7)
                    line_artists.append(line)
                    scatter_artists.append(scatter)
                    for i in range(1, len(enc_data)):
                        x1i, y1i = enc_data.iloc[i-1][['x','y']]
                        x2i, y2i = enc_data.iloc[i][['x','y']]
                        ax.arrow(
                            x1i, y1i,
                            (x2i - x1i)*0.9, (y2i - y1i)*0.9,
                            head_width=0.5, head_length=1,
                            fc='gray', ec='gray', alpha=0.5
                        )

                # Create legend first
                ax.legend()
                leg = ax.get_legend()
                if leg and line_artists:
                    leg.set_draggable(True)
                    legend_map = {}
                    for handle, line, scatter in zip(leg.legend_handles, line_artists, scatter_artists):
                        handle.set_picker(5)  # Set picker tolerance
                        legend_map[handle] = (line, scatter)

                    def on_pick(event):
                        if event.artist in legend_map:
                            line, scatter = legend_map[event.artist]
                            visible = not line.get_visible()
                            line.set_visible(visible)
                            scatter.set_visible(visible)
                            event.artist.set_alpha(1.0 if visible else 0.2)
                            fig.canvas.draw_idle()

                    fig.canvas.mpl_connect('pick_event', on_pick)
            else:
                line, = ax.plot(movement['x'], movement['y'], 'b-', alpha=0.5, label=f'Movement Path for {unit}')
                scatter = ax.scatter(movement['x'], movement['y'], c='b', alpha=0.7)
                
                # Create legend first for single path
                ax.legend()
                leg = ax.get_legend()
                if leg:
                    leg.set_draggable(True)
                    legend_map = {leg.legend_handles[0]: (line, scatter)}

            # Create legend frame with map controls
            legend_frame = ttk.Frame(self.plot_window)
            legend_frame.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Add map controls
            self.create_map_controls(legend_frame, fig, ax)

            canvas = FigureCanvasTkAgg(fig, self.plot_window)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, self.plot_window)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        except Exception as e:
            messagebox.showwarning("Movement Error", str(e))

    def prompt_average_movement(self):
        if self.df is None:
            messagebox.showwarning("Error", "Please load data first")
            return
        dialog = AverageMovementDialog(self.root)
        self.root.wait_window(dialog)
        params = dialog.get_values()
        self.plot_average_movement(params)

    def plot_average_movement(self, params):
        try:
            min_time = float(params['min_time']) if params['min_time'] else 0
            max_time = float(params['max_time']) if params['max_time'] else float('inf')
            death_threshold = int(params['death_threshold']) if params['death_threshold'] else None

            if params['unit']:
                units = [params['unit']]
            else:
                # Filter for player names ending in -EU or -US
                units = [u for u in self.df['Damage source'].dropna().unique() 
                        if isinstance(u, str) and (u.endswith('-EU') or u.endswith('-US'))]

            results = []
            for unit in units:
                unit_data = self.df[
                    ((self.df['Damage source'] == unit) | (self.df['Spell destination'] == unit)) &
                    (self.df['relative fight time (s)'] >= min_time) &
                    (self.df['relative fight time (s)'] <= max_time)
                ]
                
                # Apply death threshold filtering if specified
                if death_threshold:
                    valid_events_mask = pd.Series(False, index=unit_data.index)
                    for enc_id in unit_data['encounter id'].unique():
                        enc_data = unit_data[unit_data['encounter id'] == enc_id]
                        deaths = self.df[
                            (self.df['encounter id'] == enc_id) & 
                            (self.df['event type'] == 'UNIT_DIED')
                        ]
                        
                        if not deaths.empty and len(deaths) >= death_threshold:
                            cutoff = deaths.iloc[death_threshold-1]['timestamp']
                            valid_events_mask |= (
                                (unit_data['encounter id'] == enc_id) & 
                                (unit_data['timestamp'] <= cutoff))
                        else:
                            valid_events_mask |= (unit_data['encounter id'] == enc_id)
                    
                    unit_data = unit_data[valid_events_mask]
                
                grouped = unit_data.groupby('encounter id')
                paths = []
                try:
                    for enc_id, group in grouped:
                        path = group.sort_values('relative fight time (s)')[
                            ['relative fight time (s)','X coord','Y coord']
                        ].dropna()
                        if not path.empty:
                            paths.append(path)
                except Exception as e:
                    print(f"Error processing paths: {e}")
                    continue

                if not paths:
                    continue

                # Calculate time grid with fixed interval of 0.5 seconds
                time_interval = 0.5  # One point every 0.5 seconds
                num_points = int((max_time - min_time) / time_interval) + 1
                time_grid = np.linspace(min_time, max_time, num_points)
                
                interpolated = []
                path_data = []  # Store path data for this unit
                
                for path in paths:
                    try:
                        x_vals = path['X coord'].astype(float)
                        y_vals = path['Y coord'].astype(float)
                        t_vals = path['relative fight time (s)']
                        x_interp = np.interp(time_grid, t_vals, x_vals)
                        y_interp = np.interp(time_grid, t_vals, y_vals)
                        interpolated.append(np.column_stack((x_interp, y_interp)))
                    except:
                        continue

                if not interpolated:
                    continue
                stacked = np.stack(interpolated)
                avg_path = np.mean(stacked, axis=0)
                deviations = np.linalg.norm(stacked - avg_path, axis=2)
                std_dev = np.mean(np.std(deviations, axis=0))
                variance = np.mean(np.var(deviations, axis=0))

                # Store all paths and grouped data for this unit
                results.append((unit, std_dev, variance, avg_path, stacked, grouped))

            if not results:
                raise ValueError("No valid movement data found")
            results.sort(key=lambda x: x[1], reverse=True)

            if self.plot_window:
                self.plot_window.destroy()
            self.plot_window = tk.Toplevel(self.root)
            self.plot_window.title(f"Average Movement Paths ({min_time}-{max_time}s)")
            fig = Figure(figsize=(12, 8))
            ax = fig.add_subplot(111)

            # Plot the map if available
            if self.map_image is not None:
                try:
                    img = np.array(self.map_image)
                    h_orig, w_orig, *_ = img.shape
                    
                    map_scale = float(self.map_scale_var.get())
                    map_rotation = float(self.map_rotation_var.get())
                    map_offset_x = float(self.map_offset_x.get())
                    map_offset_y = float(self.map_offset_y.get())
                    
                    pil_img = Image.fromarray(img)
                    if map_rotation != 0:
                        pil_img = pil_img.rotate(map_rotation, expand=True, resample=Image.BICUBIC)
                    
                    map_w = int(w_orig * map_scale)
                    map_h = int(h_orig * map_scale)
                    pil_img = pil_img.resize((map_w, map_h), Image.LANCZOS)
                    img_small = np.array(pil_img)
                    
                    ax.imshow(img_small, extent=[map_offset_x, map_offset_x + map_w, 
                                               map_offset_y + map_h, map_offset_y],
                             alpha=0.5, zorder=1)
                except Exception as e:
                    print(f"Error displaying map: {e}")

            # Plot boss position if coordinates are provided
            if self.boss_x.get() and self.boss_y.get():
                try:
                    bx = float(self.boss_x.get())
                    by = float(self.boss_y.get())
                    ax.scatter(bx, by, s=200, marker='*',
                             color='gold', edgecolor='black',
                             zorder=10, label='Boss Position')
                except ValueError:
                    pass

            cmap = plt.get_cmap('tab10')
            info_lines = []
            line_artists = []
            individual_paths = {}  # Store individual path artists for each unit
            encounter_colors = {}  # Store colors for each encounter

            # First, collect all unique encounters across all units
            all_encounters = set()
            for _, _, _, _, _, unit_grouped in results:
                all_encounters.update(enc_id for enc_id, _ in unit_grouped)
            
            # Create a consistent color mapping for all encounters
            encounter_cmap = plt.get_cmap('Set3')  # Using Set3 for distinct colors
            for i, enc_id in enumerate(sorted(all_encounters)):
                encounter_colors[enc_id] = encounter_cmap(i % 12)  # Set3 has 12 colors

            for idx, (unit, std_dev, var_, avg_path, all_paths, unit_grouped) in enumerate(results):
                color = cmap(idx % 10)
                
                # Create main average path line with high zorder to stay on top
                line, = ax.plot(avg_path[:,0], avg_path[:,1], color=color, label=f"{unit} (avg)", 
                              linewidth=2, zorder=10)  # High zorder to stay on top
                line_artists.append(line)
                
                # Create individual path lines (initially hidden)
                unit_paths = []
                
                for enc_id, group in unit_grouped:
                    path = group.sort_values('relative fight time (s)')[
                        ['relative fight time (s)','X coord','Y coord']
                    ].dropna()
                    if not path.empty:
                        x_vals = path['X coord'].astype(float)
                        y_vals = path['Y coord'].astype(float)
                        
                        # Create path line with encounter-specific color and lower zorder
                        path_color = encounter_colors[enc_id]
                        path_line, = ax.plot(x_vals, y_vals, 
                                           color=path_color, 
                                           alpha=0.4, 
                                           visible=False,
                                           label=f"Enc {enc_id}",
                                           picker=True,
                                           zorder=5)  # Lower zorder to stay below average
                        
                        # Store the encounter info and time values for tooltip
                        path_line.enc_id = enc_id
                        path_line.times = path['relative fight time (s)'].values
                        path_line.coords = np.column_stack((x_vals, y_vals))
                        
                        unit_paths.append((enc_id, path_line))
                
                individual_paths[unit] = unit_paths
                info_lines.append(f"{unit}: SD={std_dev:.2f}, Var={var_:.2f}")

            # Create custom legend with collapsible dropdowns
            legend_frame = ttk.Frame(self.plot_window)
            legend_frame.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Create header frame for title and buttons
            header_frame = ttk.Frame(legend_frame)
            header_frame.pack(fill=tk.X, pady=5)
            ttk.Label(header_frame, text="Toggle Visibility:").pack(side=tk.LEFT, padx=5)
            
            # Add update button
            def update_plot():
                fig.canvas.draw_idle()
                canvas.draw()
            
            ttk.Button(header_frame, text="Update Plot", 
                      command=update_plot).pack(side=tk.RIGHT, padx=5)
            
            # Add toggle all units button
            all_units_var = tk.BooleanVar(value=True)
            def toggle_all_units():
                for idx, line in enumerate(line_artists):
                    line.set_visible(all_units_var.get())
                    # Update individual checkboxes
                    for widget in scrollable_frame.winfo_children():
                        if isinstance(widget, ttk.Frame):
                            for child in widget.winfo_children():
                                if isinstance(child, ttk.Frame):  # main_row
                                    for grandchild in child.winfo_children():
                                        if isinstance(grandchild, ttk.Checkbutton):
                                            grandchild.state(['!alternate'])
                                            if all_units_var.get():
                                                grandchild.state(['selected'])
                                            else:
                                                grandchild.state(['!selected'])
                update_plot()
            
            ttk.Checkbutton(header_frame, text="All Units", 
                           variable=all_units_var,
                           command=toggle_all_units).pack(side=tk.RIGHT, padx=5)

            # Create scrollable frame for units
            legend_canvas = tk.Canvas(legend_frame, width=200)  # Renamed from canvas to legend_canvas
            scrollbar = ttk.Scrollbar(legend_frame, orient="vertical", command=legend_canvas.yview)
            scrollable_frame = ttk.Frame(legend_canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: legend_canvas.configure(scrollregion=legend_canvas.bbox("all"))
            )

            legend_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            legend_canvas.configure(yscrollcommand=scrollbar.set)

            # Store frames for each unit to manage dropdown visibility
            dropdown_frames = {}

            # Create visibility controls for each unit
            try:
                for idx, (unit, std_dev, var_, avg_path, _, _) in enumerate(results):
                    color = cmap(idx % 10)
                    unit_frame = ttk.Frame(scrollable_frame)
                    unit_frame.pack(fill=tk.X, padx=5, pady=2)
                    
                    # Create main unit frame with average path toggle
                    main_row = ttk.Frame(unit_frame)
                    main_row.pack(fill=tk.X)
                    
                    # Average path toggle
                    avg_var = tk.BooleanVar(value=True)
                    def toggle_average(line, var):
                        line.set_visible(var.get())
                        update_plot()
                    
                    avg_check = ttk.Checkbutton(main_row, text=unit, 
                                              variable=avg_var,
                                              command=lambda l=line_artists[idx], v=avg_var: toggle_average(l, v))
                    avg_check.pack(side=tk.LEFT)
                    
                    # Color indicator for average
                    avg_color_label = ttk.Label(main_row, text="■", foreground='#{:02x}{:02x}{:02x}'.format(
                        int(color[0]*255), int(color[1]*255), int(color[2]*255)))
                    avg_color_label.pack(side=tk.LEFT)
                    
                    # Create dropdown button
                    dropdown_var = tk.BooleanVar(value=False)
                    dropdown_frame = ttk.Frame(unit_frame)
                    dropdown_frames[unit] = (dropdown_frame, dropdown_var)
                    
                    def toggle_dropdown(frame, var):
                        if var.get():
                            frame.pack(fill=tk.X, padx=20)
                        else:
                            frame.pack_forget()
                    
                    ttk.Checkbutton(main_row, text="▼", 
                                   variable=dropdown_var,
                                   command=lambda f=dropdown_frame, v=dropdown_var: toggle_dropdown(f, v)).pack(side=tk.RIGHT)
                    
                    # Create paths control frame
                    paths_control_frame = ttk.Frame(dropdown_frame)
                    paths_control_frame.pack(fill=tk.X)
                    
                    # Add "Toggle All Paths" checkbox with its own variable
                    all_paths_var = tk.BooleanVar(value=False)
                    def toggle_all_paths_for_unit(unit_paths, var):
                        # Update path visibility
                        for _, path_line in unit_paths:
                            path_line.set_visible(var.get())
                        # Update individual checkboxes
                        for widget in dropdown_frame.winfo_children():
                            if isinstance(widget, ttk.Frame) and widget != paths_control_frame:
                                for child in widget.winfo_children():
                                    if isinstance(child, ttk.Checkbutton):
                                        child.state(['!alternate'])
                                        if var.get():
                                            child.state(['selected'])
                                        else:
                                            child.state(['!selected'])
                        update_plot()
                    
                    ttk.Checkbutton(paths_control_frame, text="Toggle All Paths",
                                   variable=all_paths_var,
                                   command=lambda p=individual_paths[unit], v=all_paths_var: 
                                       toggle_all_paths_for_unit(p, v)).pack(side=tk.LEFT)
                    
                    # Add individual encounter toggles in dropdown
                    for enc_id, path_line in individual_paths[unit]:
                        enc_color = encounter_colors[enc_id]
                        enc_frame = ttk.Frame(dropdown_frame)
                        enc_frame.pack(fill=tk.X)
                        
                        # Create checkbox for this encounter
                        enc_var = tk.BooleanVar(value=False)
                        def toggle_encounter(line, var):
                            line.set_visible(var.get())
                            update_plot()
                        
                        ttk.Checkbutton(enc_frame, text=f"Encounter {enc_id}",
                                      variable=enc_var,
                                      command=lambda l=path_line, v=enc_var: toggle_encounter(l, v)).pack(side=tk.LEFT)
                        
                        # Add color indicator
                        enc_color_label = ttk.Label(enc_frame, text="■", foreground='#{:02x}{:02x}{:02x}'.format(
                            int(enc_color[0]*255), int(enc_color[1]*255), int(enc_color[2]*255)))
                        enc_color_label.pack(side=tk.LEFT)
            except Exception as e:
                print(f"Error creating visibility controls: {e}")
                return

            # Pack the scrollable frame
            legend_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Create tooltip annotation (hidden initially)
            tooltip = ax.annotate("",
                xy=(0, 0), xytext=(10, 10),
                textcoords="offset points",
                bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9),
                visible=False
            )

            def on_motion(event):
                if event.inaxes == ax:
                    # Check if we're near any path
                    for unit_paths in individual_paths.values():
                        for enc_id, path_line in unit_paths:
                            if path_line.get_visible():
                                cont, ind = path_line.contains(event)
                                if cont:
                                    # Find closest point
                                    xy = path_line.coords
                                    xyt = event.xdata, event.ydata
                                    d = np.sqrt(np.sum((xy - xyt)**2, axis=1))
                                    ind = np.argmin(d)
                                    
                                    # Format tooltip text
                                    tooltip_text = f"Encounter: {path_line.enc_id}\n"
                                    tooltip_text += f"Time: {path_line.times[ind]:.1f}s"
                                    
                                    # Update tooltip
                                    tooltip.set_text(tooltip_text)
                                    tooltip.xy = (xy[ind, 0], xy[ind, 1])
                                    tooltip.set_visible(True)
                                    fig.canvas.draw_idle()
                                    return
                    
                    # If no point is being hovered, hide the tooltip
                    tooltip.set_visible(False)
                    fig.canvas.draw_idle()

            fig.canvas.mpl_connect('motion_notify_event', on_motion)

            ax.set_title(f"Average Movement Paths ({min_time}-{max_time}s)")
            ax.grid(True)
            
            # Add statistics text
            fig.text(0.7, 0.5, "\n".join(info_lines), ha='left', va='center')

            canvas = FigureCanvasTkAgg(fig, self.plot_window)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, self.plot_window)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        except Exception as e:
            messagebox.showwarning("Analysis Error", str(e))

    def rotate_point(self, x, y, angle_degrees, origin=(0,0)):
        angle_rad = np.radians(angle_degrees)
        ox, oy = origin
        px, py = x - ox, y - oy
        qx = ox + np.cos(angle_rad) * px - np.sin(angle_rad) * py
        qy = oy + np.sin(angle_rad) * px + np.cos(angle_rad) * py
        return qx, qy

    def handle_image_drop(self, event):
        """Handle dropped image files"""
        file_path = event.data.strip('{}')  # Remove curly braces if present
        self.load_map_image(file_path)
    
    def select_image(self):
        """Open file dialog to select an image"""
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.load_map_image(file_path)
    
    def clear_image(self):
        """Clear the current map image"""
        self.map_image = None
        self.preview_label.config(text="Drag & Drop\nMap Image Here")
        if hasattr(self, 'preview_img_label'):
            self.preview_img_label.destroy()
            delattr(self, 'preview_img_label')
    
    def load_map_image(self, file_path):
        """Load and display the map image"""
        try:
            # Load and store the image
            image = Image.open(file_path)
            self.map_image = image
            
            # Create preview
            preview_size = (190, 140)  # Slightly smaller than frame
            preview = image.copy()
            preview.thumbnail(preview_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(preview)
            
            # Update preview
            if hasattr(self, 'preview_img_label'):
                self.preview_img_label.destroy()
            
            self.preview_img_label = ttk.Label(self.preview_frame, image=photo)
            self.preview_img_label.image = photo  # Keep a reference
            self.preview_img_label.pack(expand=True)
            
            # Hide the text label
            self.preview_label.pack_forget()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
            self.clear_image()

    def adjust_map(self, x_offset=0, y_offset=0, scale=None, rotation=None):
        """Adjust map parameters and update the plot"""
        try:
            if scale is not None:
                self.map_scale_var.set(str(scale))
            if rotation is not None:
                self.map_rotation_var.set(str(rotation))
            
            current_x = float(self.map_offset_x.get())
            current_y = float(self.map_offset_y.get())
            
            self.map_offset_x.delete(0, tk.END)
            self.map_offset_x.insert(0, str(current_x + x_offset))
            
            self.map_offset_y.delete(0, tk.END)
            self.map_offset_y.insert(0, str(current_y + y_offset))
            
            # Immediately update the plot if window exists
            if hasattr(self, 'plot_window') and self.plot_window:
                for widget in self.plot_window.winfo_children():
                    if isinstance(widget, FigureCanvasTkAgg):
                        self.update_plot(widget.figure, widget.figure.axes[0])
                        break
        except Exception as e:
            messagebox.showwarning("Adjustment Error", str(e))

    def create_map_controls(self, legend_frame, fig, ax):
        """Create map control widgets in the legend frame"""
        # Create map controls frame
        map_controls = ttk.LabelFrame(legend_frame, text="Map Controls")
        map_controls.pack(fill=tk.X, padx=5, pady=5)
        
        # Add update button at the top
        update_frame = ttk.Frame(map_controls)
        update_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Button(update_frame, text="Update Plot",
                  command=lambda: self.update_plot(fig, ax)).pack(fill=tk.X)
        
        # Visibility toggles
        visibility_frame = ttk.Frame(map_controls)
        visibility_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Map and Data visibility toggles
        map_var = tk.BooleanVar(value=True)
        data_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(visibility_frame, text="Show Map",
                      variable=map_var,
                      command=lambda: self.toggle_map_visibility(ax, map_var.get())).pack(side=tk.LEFT)
        ttk.Checkbutton(visibility_frame, text="Show Data",
                      variable=data_var,
                      command=lambda: self.toggle_data_visibility(ax, data_var.get())).pack(side=tk.LEFT)
        
        # Scale control
        scale_frame = ttk.Frame(map_controls)
        scale_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(scale_frame, text="Scale:").pack(side=tk.LEFT)
        scale_entry = ttk.Entry(scale_frame, textvariable=self.map_scale_var, width=8)
        scale_entry.pack(side=tk.LEFT, padx=5)
        
        # Rotation control
        rotation_frame = ttk.Frame(map_controls)
        rotation_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(rotation_frame, text="Rotation:").pack(side=tk.LEFT)
        rotation_entry = ttk.Entry(rotation_frame, textvariable=self.map_rotation_var, width=8)
        rotation_entry.pack(side=tk.LEFT, padx=5)
        
        # X offset control
        x_offset_frame = ttk.Frame(map_controls)
        x_offset_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(x_offset_frame, text="X Offset:").pack(side=tk.LEFT)
        x_offset_entry = ttk.Entry(x_offset_frame, width=8)
        x_offset_entry.insert(0, "10")  # Default step size
        x_offset_entry.pack(side=tk.LEFT, padx=5)
        
        def adjust_x(amount):
            try:
                step = float(x_offset_entry.get())
                current_x = float(self.map_offset_x.get())
                new_x = current_x + (amount * step)
                self.map_offset_x.delete(0, tk.END)
                self.map_offset_x.insert(0, str(new_x))
                self.update_plot(fig, ax)  # Immediate update
            except ValueError:
                pass
        
        ttk.Button(x_offset_frame, text="←", width=2,
                  command=lambda: adjust_x(-1)).pack(side=tk.LEFT)
        ttk.Button(x_offset_frame, text="→", width=2,
                  command=lambda: adjust_x(1)).pack(side=tk.LEFT)
        
        # Y offset control
        y_offset_frame = ttk.Frame(map_controls)
        y_offset_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(y_offset_frame, text="Y Offset:").pack(side=tk.LEFT)
        y_offset_entry = ttk.Entry(y_offset_frame, width=8)
        y_offset_entry.insert(0, "10")  # Default step size
        y_offset_entry.pack(side=tk.LEFT, padx=5)
        
        def adjust_y(amount):
            try:
                step = float(y_offset_entry.get())
                current_y = float(self.map_offset_y.get())
                new_y = current_y + (amount * step)
                self.map_offset_y.delete(0, tk.END)
                self.map_offset_y.insert(0, str(new_y))
                self.update_plot(fig, ax)  # Immediate update
            except ValueError:
                pass
        
        ttk.Button(y_offset_frame, text="↑", width=2,
                  command=lambda: adjust_y(-1)).pack(side=tk.LEFT)
        ttk.Button(y_offset_frame, text="↓", width=2,
                  command=lambda: adjust_y(1)).pack(side=tk.LEFT)

    def toggle_data_visibility(self, ax, show_data):
        """Toggle the visibility of data points and lines"""
        for collection in ax.collections:  # For scatter plots
            collection.set_visible(show_data)
        for line in ax.lines:  # For line plots
            line.set_visible(show_data)
        ax.figure.canvas.draw_idle()

    def save_map_settings(self):
        """Save current map settings to a file"""
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Save Map Settings"
            )
            if file_path:
                settings = {
                    'scale': self.map_scale_var.get(),
                    'rotation': self.map_rotation_var.get(),
                    'offset_x': self.map_offset_x.get(),
                    'offset_y': self.map_offset_y.get()
                }
                with open(file_path, 'w') as f:
                    for key, value in settings.items():
                        f.write(f"{key}={value}\n")
                messagebox.showinfo("Success", "Map settings saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings:\n{str(e)}")

    def load_map_settings(self):
        """Load map settings from a file"""
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Load Map Settings"
            )
            if file_path:
                with open(file_path, 'r') as f:
                    settings = {}
                    for line in f:
                        key, value = line.strip().split('=')
                        settings[key] = value
                
                # Apply the loaded settings
                self.map_scale_var.set(settings.get('scale', '1.0'))
                self.map_rotation_var.set(settings.get('rotation', '0'))
                self.map_offset_x.delete(0, tk.END)
                self.map_offset_x.insert(0, settings.get('offset_x', '0'))
                self.map_offset_y.delete(0, tk.END)
                self.map_offset_y.insert(0, settings.get('offset_y', '0'))
                
                # Update plot if it exists
                if hasattr(self, 'plot_window') and self.plot_window and self.plot_window.winfo_exists():
                    for widget in self.plot_window.winfo_children():
                        if isinstance(widget, FigureCanvasTkAgg):
                            self.update_plot(widget.figure, widget.figure.axes[0])
                            break
                
                messagebox.showinfo("Success", "Map settings loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load settings:\n{str(e)}")

    def plot_reference_data(self):
        """Plot casting data across all encounters for map alignment"""
        if self.df is None:
            messagebox.showwarning("Error", "Please load data first")
            return

        try:
            # Use casting events for reference
            filtered = self.df[self.df['event type'].isin(['SPELL_CAST_SUCCESS', 'SWING_DAMAGE'])]
            
            if self.plot_window:
                self.plot_window.destroy()
            self.plot_window = tk.Toplevel(self.root)
            self.plot_window.title("Map Alignment Reference")

            fig = Figure(figsize=(10, 6))
            ax = fig.add_subplot(111)

            # Plot the map if available
            if self.map_image is not None:
                try:
                    img = np.array(self.map_image)
                    h_orig, w_orig, *_ = img.shape
                    
                    map_scale = float(self.map_scale_var.get())
                    map_rotation = float(self.map_rotation_var.get())
                    map_offset_x = float(self.map_offset_x.get())
                    map_offset_y = float(self.map_offset_y.get())
                    
                    pil_img = Image.fromarray(img)
                    if map_rotation != 0:
                        pil_img = pil_img.rotate(map_rotation, expand=True, resample=Image.BICUBIC)
                    
                    map_w = int(w_orig * map_scale)
                    map_h = int(h_orig * map_scale)
                    pil_img = pil_img.resize((map_w, map_h), Image.LANCZOS)
                    img_small = np.array(pil_img)
                    
                    ax.imshow(img_small, extent=[map_offset_x, map_offset_x + map_w, 
                                               map_offset_y + map_h, map_offset_y],
                             alpha=0.5, zorder=1)
                except Exception as e:
                    print(f"Error displaying map: {e}")

            # Plot the data points
            x_coords = pd.to_numeric(filtered['X coord'], errors='coerce')
            y_coords = pd.to_numeric(filtered['Y coord'], errors='coerce')
            valid = x_coords.notna() & y_coords.notna()
            
            ax.scatter(x_coords[valid], y_coords[valid], alpha=0.3, color='blue', s=1)

            # Store the current plot parameters
            self.last_plot_params = {
                'plot_type': 'scatter',
                'filtered_data': filtered,
                'encounter_ids': [],
                'data_scale': 1.0,
                'data_rotation': 0
            }

            # Create legend frame with map controls
            legend_frame = ttk.Frame(self.plot_window)
            legend_frame.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Add map controls
            self.create_map_controls(legend_frame, fig, ax)

            canvas = FigureCanvasTkAgg(fig, self.plot_window)
            canvas.draw()
            toolbar = NavigationToolbar2Tk(canvas, self.plot_window)
            toolbar.update()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showwarning("Plot Error", str(e))

    def get_color_palette(self, num_colors):
        """Generate a color palette with the specified number of distinct colors"""
        base_colors = plt.cm.tab20(np.linspace(0, 1, 20))  # Get 20 colors from tab20
        if num_colors <= 20:
            return base_colors[:num_colors]
        
        # If we need more than 20 colors, create additional variations
        extra_colors = plt.cm.Set3(np.linspace(0, 1, num_colors - 20))
        return np.vstack([base_colors, extra_colors])

class AverageMovementDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Average Movement Settings")
        self.unit = tk.StringVar()
        self.min_time = tk.StringVar()
        self.max_time = tk.StringVar()
        self.death_threshold = tk.StringVar()  # Add death threshold variable
        
        ttk.Label(self, text="Unit Name:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.unit).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="Start Time (s):").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.min_time).grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="End Time (s):").grid(row=2, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.max_time).grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self, text="Death Threshold:").grid(row=3, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.death_threshold).grid(row=3, column=1, padx=5, pady=5)
        
        ttk.Button(self, text="Plot", command=self.destroy).grid(row=4, columnspan=2, pady=10)

    def get_values(self):
        return {
            'unit': self.unit.get().strip(),
            'min_time': self.min_time.get(),
            'max_time': self.max_time.get(),
            'death_threshold': self.death_threshold.get()
        }

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = CSVVisualizer(root)
    root.mainloop()