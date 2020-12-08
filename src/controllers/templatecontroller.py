from models.templateargs import TemplateArgs

import psycopg2


#TODO: Implement all banner template logic in here including database handling

def create_template(templateArgs: TemplateArgs):

    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=database-2 user=postgres password=jojaerklam host=database-2.ca7pqa3dikbd.us-east-1.rds.amazonaws.com port=5432")
    
    # Open a cursor to perform database operations
    cursor = conn.cursor()

    # Execute a query
    cursor.execute(f"INSERT INTO a_table (name, createdDate) VALUES(%{templateArgs.name}, {templateArgs.createdDate})")
    
    #Save the change
    conn.commit()

    #Close cursor and connection
    cursor.close()
    conn.close()


def get_template(template_id: int):

    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=database-2 user=postgres password=jojaerklam host=database-2.ca7pqa3dikbd.us-east-1.rds.amazonaws.com port=5432")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"SELECT * FROM templates WHERE id={template_id}")

    # Retrieve query results
    records = cur.fetchall()

    return {"Name": "Test"}

    return records

def get_all_templates():
    
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=database-2 user=postgres password=jojaerklam host=database-2.ca7pqa3dikbd.us-east-1.rds.amazonaws.com port=5432")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM templates")

    # Retrieve query results
    records = cur.fetchall()
    
    return records


def update_template(template_id: int, templateArgs: TemplateArgs):

    return {"template name": templateArgs.name, "template id": template_id}

def delete_template(template_id: int):

    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=database-2 user=postgres password=jojaerklam host=database-2.ca7pqa3dikbd.us-east-1.rds.amazonaws.com port=5432")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute(f"DELETE FROM templates WHERE id = {template_id}")

    #Save the change
    conn.commit()

    #Close cursor and connection
    cur.close()
    conn.close()

    return {"Status" : "Success"}