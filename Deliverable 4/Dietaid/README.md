## To run the code
> 1. Set up your environment and download Django. I used this tutorial [https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment]. 
> 2. Navigate to the same directory of manage.py. 

> 3. Run the following command is any change is applied to the database or model.py: 
```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
```
> 4. Start the server with
```sh
    python3 manage.py runserver
```
> 5. Go to your web browser, and enter http://127.0.0.1:8000/ url. 

## To Do List
- Beutify Interface.
- Beutify form diplay. This might be more then editing HTML and CSS, because the form is now rendered automatically by Django with `form.as_table`.
- Security: now by entering the url with correct `diagnosis_id` or `mealplan_id`, anyone can see the diagnosis or mealplan detail. 
- Mapping diagnosis to meal plan. 
- Testing.