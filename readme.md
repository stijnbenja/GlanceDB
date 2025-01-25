# GlanceDB - View your database tables intuitively
A simple streamlit interface for viewing all the tables in your PostgreSQL database. Nothing more, nothing less.

![image](demo.png)

### Step 1
Update the DB.toml file with your credentials
```toml
dbname = "your_database_name"
user = "your_username"
password = "your_password"
host = "your_host"
port = "your_port"
```

### Step 2
Run the app locally
```bash
streamlit run app.py
```
