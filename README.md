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


Here's a simplified draft plan for the initial task:  1. **Review Requirements**: Understand the task details and goals.  2. **Setup Environment**: Prepare the development environment with necessary tools.  3. **Analyze Code**: Study the existing app code to understand its structure and functionality.  4. **Breakdown Tasks**: Divide the task into smaller parts for easier management.  5. **Estimate Time**: Estimate the time needed for each task.  6. **Create Timeline**: Plan a timeline with deadlines for completing each task.  7. **Document Plan**: Note down the breakdown, estimates, and timeline.  8. **Discuss Plan**: Share the plan with the hiring team for feedback and approval.  9. **Execute Tasks**: Work on tasks according to the plan and deadlines.  10. **Test and Review**: Test implemented features and review code for quality.  11. **Completion**: Finish the tasks within the agreed timeframe and deliver the results.  This simple plan outlines the steps to approach the task efficiently and ensure successful completion.