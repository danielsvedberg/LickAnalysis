import pandas as pd

# Load the CSV into a dataframe
df = pd.read_csv('binary_signals_events.csv')

# Subset 1: rows where base_event == 'lick'
lick_events = df[df['base_event'] == 'lick']
#rename 'edge_on' column to 'time'
lick_events = lick_events.rename(columns={'edge_on': 'time', 'base_event': 'event'})

lick_events = lick_events.loc[lick_events['duration'] < 0.11]

lick_events = lick_events[['time', 'event']]
lick_events.to_csv('lick_events.csv', index=False)


print(f"Created lick_events.csv with {len(lick_events)} rows")

# Subset 2: rows where base_event is in the specified list
target_events = ['start_tone', 'early_first_licks', 'rewarded_first_licks', 'timeout_tone']
cue_events = df[df['base_event'].isin(target_events)]
cue_events = cue_events.rename(columns={'edge_on': 'time', 'base_event': 'event'})
cue_events = cue_events.loc[((cue_events['duration'] < 0.11) | (cue_events['duration'] > 1.99)) | cue_events['duration'].isna()]
cue_events.loc[cue_events['event'].str.contains('licks', na=False), 'event'] = 'lick'
cue_events = cue_events[['time', 'event']]

# Create wideform version
cue_events_wide = pd.DataFrame()
cue_events_wide['start_tone'] = cue_events[cue_events['event'] == 'start_tone']['time'].reset_index(drop=True)
cue_events_wide['outcome'] = cue_events[cue_events['event'] != 'start_tone']['event'].reset_index(drop=True)
cue_events_wide['outcome_time'] = cue_events[cue_events['event'] != 'start_tone']['time'].reset_index(drop=True)
cue_events_wide = cue_events_wide.rename(columns={'start_tone': 'start_time'})
cue_events_wide = cue_events_wide[['start_time', 'outcome_time', 'outcome']]

cue_events.to_csv('cue_events.csv', index=False)
cue_events_wide.to_csv('trial_events.csv', index=False)
print(f"Created cue_events.csv with {len(cue_events)} rows")


print(f"\nOriginal dataframe: {len(df)} rows")
print(f"Lick events: {len(lick_events)} rows")
print(f"Cue events: {len(cue_events)} rows")