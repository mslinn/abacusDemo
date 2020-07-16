# Abacus.AI Demo

Taken from the sample code at https://abacus.ai/app/help/started

The sample Python 3 code has several bugs. 
I fixed all of them and made the following modifications:

 - Environment variable contains API key.
 - Elapsed time for each step is shown 
 - Added formatted movie recommendations

## Install Dependencies
```shell
yes | sudo apt install python3-pip
python3 -m pip install realityengines
```

## Make Project Directory
```shell
mkdir abacus
cd abacus
```

## Download Data
Use [aws cli](https://aws.amazon.com/cli/) to download the data, like this:

```shell
aws s3 cp s3://realityengines.exampledatasets/user_recommendations/movies_metadata.csv ./
aws s3 cp s3://realityengines.exampledatasets/user_recommendations/users_metadata.csv ./
aws s3 cp s3://realityengines.exampledatasets/user_recommendations/user_movie_ratings.csv ./
```

## Run Demo
```shell
export abacusKey='b0436727c76c4567a19959b7a8b3dd00'
python3 movieDemo.py
```

## Output
```
[ UseCase(use_case='CUSTOMER_CHURN', pretty_name='Customer Churn Prediction', description='Identify customers who are most likely to churn out of your system and send them marketing promotions/emails to retain them. Deploy a deep learning, real-time model that identifies customers who are most likely to leave and increase retention.'),
  UseCase(use_case='ENERGY', pretty_name='Real-Time Forecasting', description='Accurately forecast energy or computation usage in real-time. Make downstream planning decision based on your predictions. We use generative modeling and deep learning to augment your dataset with synthetic data. This unique approach allows us to make accurate predictions in real-time, even when you have little historical data.'),
  UseCase(use_case='FINANCIAL_METRICS', pretty_name='Financial Metrics Forecasting', description='Accurately plan your cash flow, revenue and sales with state-of-the-art deep learning-based forecasting. We use generative modeling and deep learning to augment your dataset with synthetic data. This unique approach allows us to make accurate predictions, even when you have little historical data.'),
  UseCase(use_case='FRAUD_ACCOUNT', pretty_name='Account Takeover and Defense', description="Shield your customers from account takeovers by blocking bots and fake sign-ups. Behind the scenes, our AI engine will develop a custom deep learning model for you that prevents bot attacks and stops account takeovers in real-time. Setup is super simple and doesn't require any ML expertise."),
  UseCase(use_case='FRAUD_THREAT', pretty_name='Intelligent Threat Detection', description="Stop breachers in their tracks by continuously monitoring your environment for malicious activity - Prevent alert fatigue by reducing the number of false positives over time. Behind the scenes, our AI engine develops a custom deep learning model that continuously monitors all your logs and alerts you of any malicious activity. Setup is super simple and doesn't require any ML expertise."),
  UseCase(use_case='FRAUD_TRANSACTIONS', pretty_name='Transaction Fraud', description="Accept payments with confidence, reduce chargebacks and catch payment fraud as it happens. Behind the scenes, our AI engine develops a custom deep learning model for you that prevents transaction fraud and catches fraudsters in real-time. Set up is super-simple and doesn't require any ML expertise"),
  UseCase(use_case='OPERATIONS_CLOUD', pretty_name='Cloud Spend Alerts', description='Deploy our state-of-the-art deep learning model to monitor your cloud spend, spot anomalies, spot runaway incidents, mitigate cost incidents, and get alerts so they can be remedied quickly. Use deep learning to find anomalies in your cloud usage and get alerts on them so that you can mitigate cost incidents.'),
  UseCase(use_case='OPERATIONS_INCIDENT', pretty_name='Early Incident Detection', description='Deploy our state-of-the-art deep learning model to detect IT incidents BEFORE they happen and increase uptime. Reduce alert fatigue and increase the efficiency of your operations team. Use deep learning to find anomalies in all your IT logs, get alerts and mitigate IT incidents. No ML expertise is required, and it takes minutes to set up.'),
  UseCase(use_case='PERS_PROMOTIONS', pretty_name='Personalized Promotions', description='Send personalized promotions to your customers and increase engagement - Personalize promotions based on catalog items, marketing messages, delivery channels and discount terms. Deploy a deep-learning real-time model that targets relevant promotions to customers and increases engagement. No ML expertise is required, and setup is easy.'),
  UseCase(use_case='PREDICTING', pretty_name='Predictive Modeling', description='Use historical data to predict future occurrences. Create your custom state-of-the-art predictive model and deploy it in production in hours, not months!. You can create a custom model for your specific needs simply by specifying your inputs/outputs and pointing us to the data. Our master AI will do the data processing, algorithm selection, model creation, and deploy the model in production for you.'),
  UseCase(use_case='RETAIL', pretty_name='Demand Forecasting', description='Accurately forecast retail demand. We use generative modeling and deep learning to augment your dataset with synthetic data. This allows us to make accurate predictions even when you have little historical data.'),
  UseCase(use_case='SALES_FORECASTING', pretty_name='Sales and Revenue Forecasting', description='Forecast sales and revenue across your sales reps, products, business units and locations. Use deep learning to forecast your sales across multiple dimensions. Make better planning discussions and anticipate future problems so you can mitigate them.'),
  UseCase(use_case='SALES_SCORING', pretty_name='Predictive Lead Scoring', description='Identify the sales leads that are most likely convert into paying customers and increase revenue. Just point our AI engine to your data, and we will create a custom deep learning model that will score all your leads and identify the best ones for conversion.'),
  UseCase(use_case='USER_RANKINGS', pretty_name='Personalized Re-Ranking of Lists', description='Re-rank search results or list of items based on a user preferences. Maximize user engagement and revenue. Our unique blend of reinforcement learning and deep learning-based technology works even when you have little historical data and have to deal with a fast-changing catalog or multiple new users.'),
  UseCase(use_case='USER_RECOMMENDATIONS', pretty_name='Personalized Recommendations', description='Increase user engagement and revenue with personalized recommendations on your app/website. Our unique blend of reinforcement learning and deep learning-based technology works even when you have little historical data and have to deal with a fast-changing catalog or multiple new users.'),
  UseCase(use_case='USER_RELATED', pretty_name='Related Items', description='Maximize revenue and user engagement. Immerse your customers into your app/website by providing them with a rich browse and related items experience. Our unique blend of reinforcement learning and deep learning-based technology works even when you have little historical data and have to deal with a fast-changing catalog or multiple new users.')]
Created project in 1.22 seconds
Movies Dataset Uploaded
Uploaded movies_metadata.csv in 1.52 seconds
Users Dataset Uploaded
Uploaded users_metadata.csv in 1.67 seconds
User Movie Ratings Dataset Uploaded
Uploaded user_movie_ratings.csv in 13.38 seconds
Movies Schema:
[ Schema(name='movie_id', column_mapping='ITEM_ID', column_data_type='IDENTIFIER'),
  Schema(name='movie', column_mapping=None, column_data_type='CATEGORICAL'),
  Schema(name='genres', column_mapping=None, column_data_type='CATEGORICAL')]
Users Schema:
[ Schema(name='user_id', column_mapping='USER_ID', column_data_type='IDENTIFIER'),
  Schema(name='gender', column_mapping=None, column_data_type='CATEGORICAL'),
  Schema(name='age', column_mapping=None, column_data_type='CATEGORICAL'),
  Schema(name='occupation', column_mapping=None, column_data_type='CATEGORICAL'),
  Schema(name='zip_code', column_mapping=None, column_data_type='CATEGORICAL')]
User Movie Ratings Schema:
[ Schema(name='user_id', column_mapping='USER_ID', column_data_type='IDENTIFIER'),
  Schema(name='movie_id', column_mapping='ITEM_ID', column_data_type='IDENTIFIER'),
  Schema(name='rating', column_mapping=None, column_data_type='CATEGORICAL'),
  Schema(name='timestamp', column_mapping='TIMESTAMP', column_data_type='TIMESTAMP')]
Pretty printed datasets in 28.21 seconds
Validated project in 0.18 seconds
Trained model in 0.35 seconds
Created dictionary from model in 0.00 seconds
Evaluated model in 3094.25 seconds
ModelMetrics(model_id='6df745032', model_version='11be5694b8', metrics={'ndcg': 0.3376615979628106, 'ndcg@5': 0.25403052944765353, 'ndcg@10': 0.28526823325922424, 'map': 0.06146667207077936, 'map@5': 0.08530601092896174, 'map@10': 0.06939175859323693, 'mrr': 0.24895138584790816, 'coverage': 0.4825926974242853}, baseline_metrics=None)
Displayed model metrics in 0.23 seconds
Deployed model in 74.29 seconds
Deployment token = c3c7b226e973425c9fc84d28f208115b
[ {'_activation': 0.03476132079958916, 'movie_id': '3408'},
  {'_activation': 0.0333285816013813, 'movie_id': '3753'},
  {'_activation': 0.02898501046001911, 'movie_id': '3512'},
  {'_activation': 0.027437668293714523, 'movie_id': '3185'},
  {'_activation': 0.027203701436519623, 'movie_id': '3755'},
  {'_activation': 0.024596603587269783, 'movie_id': '2997'},
  {'_activation': 0.023847518488764763, 'movie_id': '3536'},
  {'_activation': 0.023307960480451584, 'movie_id': '3114'},
  {'_activation': 0.019718218594789505, 'movie_id': '3751'},
  {'_activation': 0.01719195581972599, 'movie_id': '3510'},
  {'_activation': 0.015038423240184784, 'movie_id': '3555'},
  {'_activation': 0.014687862247228622, 'movie_id': '3916'},
  {'_activation': 0.014247424900531769, 'movie_id': '2858'},
  {'_activation': 0.013394530862569809, 'movie_id': '3578'},
  {'_activation': 0.012044749222695827, 'movie_id': '3189'},
  {'_activation': 0.010466653853654861, 'movie_id': '3481'},
  {'_activation': 0.010053599253296852, 'movie_id': '3948'},
  {'_activation': 0.009951898828148842, 'movie_id': '3176'},
  {'_activation': 0.009876996278762817, 'movie_id': '3147'},
  {'_activation': 0.008573571220040321, 'movie_id': '3534'},
  {'_activation': 0.008417443372309208, 'movie_id': '3827'},
  {'_activation': 0.008063478395342827, 'movie_id': '3157'},
  {'_activation': 0.008046126924455166, 'movie_id': '3798'},
  {'_activation': 0.007715740706771612, 'movie_id': '3155'},
  {'_activation': 0.007356259040534496, 'movie_id': '3148'},
  {'_activation': 0.007319536060094833, 'movie_id': '3623'},
  {'_activation': 0.007176732178777456, 'movie_id': '3893'},
  {'_activation': 0.006084125954657793, 'movie_id': '1259'},
  {'_activation': 0.0060509610921144485, 'movie_id': '3513'},
  {'_activation': 0.0057734595611691475, 'movie_id': '3624'},
  {'_activation': 0.005744836293160915, 'movie_id': '3160'},
  {'_activation': 0.005601371638476849, 'movie_id': '318'},
  {'_activation': 0.005234170705080032, 'movie_id': '1148'},
  {'_activation': 0.005202693864703178, 'movie_id': '3175'},
  {'_activation': 0.004852589685469866, 'movie_id': '3081'},
  {'_activation': 0.004767708946019411, 'movie_id': '908'},
  {'_activation': 0.004695891868323088, 'movie_id': '3793'},
  {'_activation': 0.004554037004709244, 'movie_id': '3897'},
  {'_activation': 0.0038892023731023073, 'movie_id': '3516'},
  {'_activation': 0.0038653176743537188, 'movie_id': '3179'},
  {'_activation': 0.0037333762738853693, 'movie_id': '3615'},
  {'_activation': 0.0034547559916973114, 'movie_id': '3844'},
  {'_activation': 0.0034514379221946, 'movie_id': '3911'},
  {'_activation': 0.003438381478190422, 'movie_id': '1304'},
  {'_activation': 0.003435689490288496, 'movie_id': '3565'},
  {'_activation': 0.0033672081772238016, 'movie_id': '1234'},
  {'_activation': 0.00328559591434896, 'movie_id': '3298'},
  {'_activation': 0.0032546864822506905, 'movie_id': '3301'},
  {'_activation': 0.003108921693637967, 'movie_id': '589'},
  {'_activation': 0.003049021353945136, 'movie_id': '3186'}]

Formatted Recommendations
3408 "Erin Brockovich (2000)" 0.03476132079958916
3753 "Patriot, The (2000)" 0.0333285816013813
3512 "Return to Me (2000)" 0.02898501046001911
3185 "Snow Falling on Cedars (1999)" 0.027437668293714523
3755 "Perfect Storm, The (2000)" 0.027203701436519623
2997 "Being John Malkovich (1999)" 0.024596603587269783
3536 "Keeping the Faith (2000)" 0.023847518488764763
3114 "Toy Story 2 (1999)" 0.023307960480451584
3751 "Chicken Run (2000)" 0.019718218594789505
3510 "Frequency (2000)" 0.01719195581972599
3555 "U-571 (2000)" 0.015038423240184784
3916 "Remember the Titans (2000)" 0.014687862247228622
2858 "American Beauty (1999)" 0.014247424900531769
3578 "Gladiator (2000)" 0.013394530862569809
3189 "My Dog Skip (1999)" 0.012044749222695827
3481 "High Fidelity (2000)" 0.010466653853654861
3948 "Meet the Parents (2000)" 0.010053599253296852
3176 "Talented Mr. Ripley, The (1999)" 0.009951898828148842
3147 "Green Mile, The (1999)" 0.009876996278762817
3534 "28 Days (2000)" 0.008573571220040321
3827 "Space Cowboys (2000)" 0.008417443372309208
3157 "Stuart Little (1999)" 0.008063478395342827
3798 "What Lies Beneath (2000)" 0.008046126924455166
3155 "Anna and the King (1999)" 0.007715740706771612
3148 "Cider House Rules, The (1999)" 0.007356259040534496
3623 "Mission: Impossible 2 (2000)" 0.007319536060094833
3893 "Nurse Betty (2000)" 0.007176732178777456
1259 "Stand by Me (1986)" 0.006084125954657793
3513 "Rules of Engagement (2000)" 0.0060509610921144485
3624 "Shanghai Noon (2000)" 0.0057734595611691475
3160 "Magnolia (1999)" 0.005744836293160915
318 "Shawshank Redemption, The (1994)" 0.005601371638476849
1148 "Wrong Trousers, The (1993)" 0.005234170705080032
3175 "Galaxy Quest (1999)" 0.005202693864703178
3081 "Sleepy Hollow (1999)" 0.004852589685469866
908 "North by Northwest (1959)" 0.004767708946019411
3793 "X-Men (2000)" 0.004695891868323088
3897 "Almost Famous (2000)" 0.004554037004709244
3516 "Bell, Book and Candle (1958)" 0.0038892023731023073
3179 "Angela's Ashes (1999)" 0.0038653176743537188
3615 "Dinosaur (2000)" 0.0037333762738853693
3844 "Steel Magnolias (1989)" 0.0034547559916973114
3911 "Best in Show (2000)" 0.0034514379221946
1304 "Butch Cassidy and the Sundance Kid (1969)" 0.003438381478190422
3565 "Where the Heart Is (2000)" 0.003435689490288496
1234 "Sting, The (1973)" 0.0033672081772238016
3298 "Boiler Room (2000)" 0.00328559591434896
3301 "Whole Nine Yards, The (2000)" 0.0032546864822506905
589 "Terminator 2: Judgment Day (1991)" 0.003108921693637967
3186 "Girl, Interrupted (1999)" 0.003049021353945136
```
