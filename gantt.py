import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

# --- Data Preparation ---
# Tasks based on the flowchart (Page 15 of the PDF)
# Assuming Year 2025 based on Page 3
tasks_data = [
    {"Task": "Brainstorming", "Start": "2025-02-03", "Duration_days": 1},
    {"Task": "Concept Development", "Start": "2025-02-04", "Duration_days": 2}, # Assumed duration
    {"Task": "Choosing Product", "Start": "2025-02-05", "Duration_days": 1},
    {"Task": "Market Research", "Start": "2025-02-06", "Duration_days": 3}, # Assumed duration/parallel
    {"Task": "Product Proposal", "Start": "2025-02-06", "Duration_days": 5}, # Feb 6 to Feb 10
    {"Task": "Customer Validation", "Start": "2025-02-09", "Duration_days": 4}, # Assumed duration after Mkt Res
    {"Task": "Product Approval", "Start": "2025-02-10", "Duration_days": 1}, # Milestone
    {"Task": "Gathering RRLs & RRS", "Start": "2025-02-13", "Duration_days": 1},
    {"Task": "Design & Planning", "Start": "2025-02-14", "Duration_days": 7}, # Assumed duration
    {"Task": "Draft Sketch", "Start": "2025-02-21", "Duration_days": 1}, # Milestone or short task
    {"Task": "Materials & Costing", "Start": "2025-02-24", "Duration_days": 10}, # Feb 24 to Mar 5 (approx)
    {"Task": "Material Procurement", "Start": "2025-03-06", "Duration_days": 5}, # Parallel with Proto Dev start
    {"Task": "Prototype Development", "Start": "2025-03-06", "Duration_days": 22}, # Mar 6 to Mar 27 (interpreting 36 as end March)
    {"Task": "Testing & Calibration", "Start": "2025-03-28", "Duration_days": 1},
    # --- Assuming an "Adjustments" phase if needed ---
    {"Task": "Final Adjustments", "Start": "2025-03-29", "Duration_days": 3}, # Assumed path if adjustments needed
    {"Task": "Marketing Strategy Dev", "Start": "2025-03-15", "Duration_days": 19}, # Assumed duration, partially parallel
    # --- Assuming Production starts after Adjustments/Testing ---
    {"Task": "Production", "Start": "2025-04-01", "Duration_days": 14}, # Assumed duration
    {"Task": "Distribution", "Start": "2025-04-15", "Duration_days": 6}, # Assumed duration
    # --- Placing Deployment & Demo chronologically ---
    {"Task": "Deployment & Demo", "Start": "2025-04-21", "Duration_days": 3}, # Moved from Apr 3 to follow sequence
]

# Convert string dates to datetime objects and calculate end dates
for task in tasks_data:
    task['Start_Date'] = datetime.strptime(task['Start'], '%Y-%m-%d')
    task['End_Date'] = task['Start_Date'] + timedelta(days=task['Duration_days'] -1 ) # Inclusive end day
    task['Duration'] = timedelta(days=task['Duration_days'])

# Extract data for plotting
tasks = [t['Task'] for t in tasks_data]
starts = [mdates.date2num(t['Start_Date']) for t in tasks_data]
durations = [t['Duration_days'] for t in tasks_data] # Use numeric duration for barh width

# Assign y-positions (indices)
y_pos = np.arange(len(tasks))

# --- Plotting ---
fig, ax = plt.subplots(figsize=(12, 8)) # Adjust figure size as needed

# Create the horizontal bars (Gantt bars)
colors = plt.cm.viridis(np.linspace(0, 1, len(tasks))) # Or plt.cm.tab20, etc.
ax.barh(y_pos, durations, left=starts, height=0.6, align='center', color=colors, alpha=0.8)

# --- Formatting ---
# Set y-axis ticks and labels
ax.set_yticks(y_pos)
ax.set_yticklabels(tasks)
ax.invert_yaxis()  # Invert y-axis to have the first task at the top

# Format the x-axis (timeline)
ax.xaxis_date() # Treat x-axis as dates
date_format = mdates.DateFormatter('%Y-%m-%d') # Define date format
ax.xaxis.set_major_formatter(date_format)

# Set major ticks locator (e.g., every week or every few days)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1)) # Show every Monday
ax.xaxis.set_minor_locator(mdates.DayLocator()) # Show minor ticks for days

fig.autofmt_xdate() # Auto-rotate date labels for better readability

# Add grid lines
ax.grid(True, axis='x', linestyle='--', alpha=0.6)

# Add labels and title
ax.set_xlabel("Timeline")
ax.set_ylabel("Tasks")
ax.set_title("Drip-o-matic Project Gantt Chart (Based on Development Flowchart)")

# Add Task Durations on Bars (Optional)
# for i, task_data_item in enumerate(tasks_data):
#     bar_start = mdates.date2num(task_data_item['Start_Date'])
#     bar_duration = task_data_item['Duration_days']
#     text_x = bar_start + bar_duration / 2
#     text_y = y_pos[i]
#     # Check if duration is large enough to display text inside
#     if bar_duration > 2:
#         ax.text(text_x, text_y, f"{bar_duration}d", va='center', ha='center', color='white', fontsize=8)
#     elif bar_duration > 0: # Put text outside for very short bars
#          ax.text(bar_start + bar_duration + 0.2 , text_y, f"{bar_duration}d", va='center', ha='left', color='black', fontsize=8)


plt.tight_layout() # Adjust layout to prevent labels overlapping

# --- SAVE THE PLOT AS AN IMAGE FILE ---
# This line saves the figure before showing it.
# You can change the filename and extension (e.g., .jpg, .pdf, .svg)
plt.savefig('drip-o-matic_gantt_chart.png', dpi=300)
print("Gantt chart saved as drip-o-matic_gantt_chart.png")

# --- DISPLAY THE PLOT (Optional after saving) ---
plt.show()
