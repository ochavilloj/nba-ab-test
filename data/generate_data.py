import numpy as np
import pandas as pd

np.random.seed(42)
n_users = 10000

df = pd.DataFrame({
    'user_id': range(n_users),
    'group': np.where(np.random.rand(n_users) < 0.5, 'control', 'treatment'),
    'platform': np.random.choice(['iOS', 'Android'], n_users, p=[0.6, 0.4]),
    'user_tenure_days': np.random.exponential(scale=180, size=n_users).astype(int),
    'games_watched_30d': np.random.poisson(lam=6, size=n_users),
    'favorite_team_playing': np.random.choice([True, False], n_users, p=[0.35, 0.65])
})

# Control: notification at halftime (~18% CTR)
# Treatment: notification at 4th quarter when game is close (~23% CTR)
base_ctr = 0.18
lift = 0.05

df['clicked'] = df.apply(lambda row:
    int(np.random.rand() < (base_ctr + lift +
        0.03 * row['favorite_team_playing'] +
        0.01 * (row['games_watched_30d'] > 8)))
    if row['group'] == 'treatment'
    else int(np.random.rand() < base_ctr), axis=1)

df['session_duration_sec'] = np.where(
    df['clicked'] == 1,
    np.random.normal(loc=420, scale=90, size=n_users),
    np.random.normal(loc=180, scale=60, size=n_users)
).clip(min=0).astype(int)

df.to_csv('data/nba_notifications_experiment.csv', index=False)
print("Dataset created successfully!")
print(df.groupby('group')[['clicked', 'session_duration_sec']].mean())