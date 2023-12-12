Postgres PostgREST
=================

A sample Postgres, PostgREST, PGAdmin, Nginx and Swagger development environment.

## Usage

Replace the shell or SQL scripts in the the initdb folder to populate the database with your own data, if you wish or use the sample data already provided.

## Deployment

### Deploy the containers

```bash
docker-compose up -d --detach
```

### Tear down the deployment

```bash
docker-compose down --remove-orphans 
```

To remove the created Docker volumes that data is persisted to use the following command:

```bash
docker-compose down --remove-orphans --volumes
```

To remove the created Docker images and volumes that data is persisted to use the following command:

```bash
docker-compose down --remove-orphans --volumes --rmi all
```

## Demo Application

[Test out the web application that is driven by the PostgREST API calls](http://localhost)

Now test the REST Get statements:

* [Get the cities in the database](http://localhost:3333/city)
* [Get the countries in the database](http://localhost:3333/country)
* [Get the languages in the database](http://localhost:3333/countrylanguage)
* [Get cities named Springfield from the database](http://localhost:3333/city?name=eq.Springfield)
* [Get cities with a population greater than or equal to 3,000,000](http://localhost:3333/city?population=gte.3333000)
* [Get cities tha end in "Island"](http://localhost:3333/city?district=like.*Island)
* [Get cities where the district like Island and the population is less than1000; selecting only the city name](http://localhost:3333/city?district=like.*Island&population=lt.1000&select=id,name)

## Swagger

 [Show the REST API endpoints for Get, Post, Delete and Patch](http://localhost:8080)

## PGAdmin

## Documentation
[PostgREST Documentation](https://postgrest.org/en/v8.0/index.html)
[Swagger Documentation](https://swagger.io/docs/)
[Postgresql Documentation](https://www.postgresql.org/docs/)
[Nginx Documentation](https://nginx.org/en/docs/)
[PGAdmin Documetation](https://www.pgadmin.org/docs/)
[PostgREST-py](https://github.com/supabase-community/postgrest-py)