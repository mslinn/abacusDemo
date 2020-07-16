# This is an improved version of the sample code at https://abacus.ai/app/help/started
# Mike Slinn mslinn@empathyworks.ai

import csv, os, pprint, time
from realityengines.client import ReClient

def show_time(message, time2, time1):
    print(f"{message} in {(time2 - time1):.2f} seconds")

time0 = time.time()

api_key = os.environ.get('abacusKey')
data_dir = './'

pp = pprint.PrettyPrinter(indent=2)  # The formatting configuration for the pretty print tool.

client = ReClient(api_key)

use_cases = client.list_use_cases()
pp.pprint(use_cases)

project = client.create_project(name='example movie recommendations', use_case='USER_RECOMMENDATIONS')
client.describe_use_case_requirements('USER_RECOMMENDATIONS')

time1 = time.time()
show_time("Created project", time1, time0)

movies_upload = client.create_dataset_from_local_file('Movies',
                                                      project_id=project.project_id,
                                                      dataset_type='CATALOG_ATTRIBUTES')

with open(data_dir + 'movies_metadata.csv') as file:
   movies_dataset = movies_upload.upload_file(file)

time2 = time.time()
show_time("Uploaded movies_metadata.csv", time2, time1)

users_upload = client.create_dataset_from_local_file('Users',
                                                     project_id=project.project_id,
                                                     dataset_type='USER_ATTRIBUTES')

with open(data_dir + 'users_metadata.csv') as file:
   users_dataset = users_upload.upload_file(file)

time3 = time.time()
show_time("Uploaded users_metadata.csv", time3, time2)

user_movie_ratings_upload = client.create_dataset_from_local_file('User Movie Ratings',
                                                                  project_id=project.project_id,
                                                                  dataset_type='USER_ITEM_INTERACTIONS')
with open(data_dir + 'user_movie_ratings.csv') as file:
   user_movie_ratings_dataset = user_movie_ratings_upload.upload_file(file)

time4 = time.time()
show_time("Uploaded user_movie_ratings.csv", time4, time3)

datasets = [movies_dataset, users_dataset, user_movie_ratings_dataset]

for dataset in datasets:
   dataset.wait_for_inspection()
   print(f'{dataset.name} Schema:')
   pp.pprint(client.get_schema(project.project_id, dataset.dataset_id))

time5 = time.time()
show_time("Pretty printed datasets", time5, time4)

project.validate()

time6 = time.time()
show_time("Validated project", time6, time5)

model = project.train_model()

time7 = time.time()
show_time("Trained model", time7, time6)

model.to_dict()

time8 = time.time()
show_time("Created dictionary from model", time8, time7)

model.wait_for_evaluation()  # this took 10 minutes 

time9 = time.time()
show_time("Evaluated model", time9, time8)

pp.pprint(model.get_metrics())

time10 = time.time()
show_time("Displayed model metrics", time10, time9)

deployment = model.create_deployment('My first model deployment')
deployment.wait_for_deployment()  # it can take a minute or two for a deployment to be ready

time11 = time.time()
show_time("Deployed model", time11, time10)

deployment_token = project.create_deployment_token().deployment_token
print("Deployment token = " + deployment_token)

recommendations = client.get_recommendations(deployment_token=deployment_token,
                           deployment_id=deployment.deployment_id,
                           query_data= { "user_id" : "1107" } 
                          )
pp.pprint(recommendations)

print("\nFormatted Recommendations")

with open(data_dir + 'movies_metadata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    movie_list = [record for record in reader]

def find_movie(movie_id):
   return [record for record in movie_list if record['movie_id'] == movie_id]
   
for r in recommendations:
    movie = find_movie(r['movie_id'])
    for m in movie:
        print(r['movie_id'], '"' + m['movie'] + '"', r['_activation'])

time12 = time.time()
show_time("Retrieved recommendations", time12, time11)
show_time("Total elaped time", time12, time0)
