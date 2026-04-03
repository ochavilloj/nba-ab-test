# NBA Push Notification A/B Test

## Business Question
Does sending contextual push notifications during high-leverage 4th quarter 
moments drive higher engagement than standard halftime notifications?

## Result
Treatment group showed a 27.8% relative lift in CTR (18.0% → 23.0%, 
p < 0.001). Effect was strongest among users whose favorite team was 
playing (+34% lift). Recommending full rollout with personalization layer.

## Methods
- Two-proportion z-test (α = 0.05)
- Power analysis & sample size calculation
- Sample Ratio Mismatch (SRM) check
- Segment analysis across platform and user engagement tier
- Secondary metric: session duration (t-test)

## Dashboard
[View Tableau Dashboard]((https://public.tableau.com/views/NBAPushNotificationABTestEngagementAnalysis/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link))

## Project Structure
nba_ab_test/
├── data/
│   ├── generate_data.py
│   ├── nba_notifications_experiment.csv
│   └── nba_notifications_tableau.csv
├── notebooks/
│   └── ab_test_analysis.ipynb
├── dashboard/
│   └── (chart exports)
└── README.md

## Skills Demonstrated
- Python (Pandas, NumPy, SciPy, Statsmodels)
- Experimental design & A/B testing
- Statistical significance testing
- Segmentation analysis
- Tableau dashboard
