# docker assignment 2 part 2 
## muhammad affan 

# Access Web Application
 To build and run the application, use the following command:

```bash
    docker build .  
```
open a web browser and navigate to http://localhost to access the web application. You should see a "Hello World!" message

# Including database
i include the necessary dependencies to run the database

# Creating docker-compose.yml
defining all the services in it

# Run the application 
```bash
    docker-compose up  
```
# Add New Feature
add new printout function in app.py 
```bash
@app.route("/new-feature") 
def new_feature():
    return "adding new feature a new feature!"
```
# Backup Strategy
Docker volume has been defined for the PostgreSQL database for implementing a backup strategy
```bash
volumes:
      - database-data:/var/lib/postgresql/data
```

# Scaling Strategy
```bash
docker-compose up --scale web=3
```
use this comman for scaling strategy

# Monitoring Strategy 
for monitoring i use Grafana and Prometheus .
Prometheus is a monitoring solution for storing time series data like metrics. Grafana allows to visualize the data stored in Prometheus