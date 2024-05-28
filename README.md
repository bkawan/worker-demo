## Installation for Local Environment

1. **Clone Repository:**
    ```bash
    git clone https://bkawan/workder-demo
    cd workker
    ```

2. **Set Up Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment:**
    ```bash
    cp config/env.example.py config/env.py
    ```
    Edit the `config/env.py` file according to your requirements.

5. **Database Setup:**
    ```bash
    python manage.py migrate
    ```

6. **Create Superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Server:**
    ```bash
    python manage.py runserver
    ```
    Open your web browser and navigate to [http://localhost:8000/](http://localhost:8000/) to access the application.


## List of APIs

1. **Units by Worker:**
   - Endpoint: `http://localhost:8000/api/v1/worker/units-by-worker/`
   - Description: Retrieves units associated with a worker.

2. **Visit API:**
   - Endpoint: `http://localhost:8000/api/v1/worker/visits/create/`
   - Description: API for creating visits.


