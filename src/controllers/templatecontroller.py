from models.templateargs import TemplateArgs

import psycopg2


#TODO: Implement all banner template logic in here including database handling

def get_template(template_id: int):

    return "Should return template with id"+template_id

def get_all_templates():
    
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=database-2 user=postgres password=jojaerklam host=database-2.ca7pqa3dikbd.us-east-1.rds.amazonaws.com port=5432")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM my_data")

    # Retrieve query results
    records = cur.fetchall()
    
    return records


def update_template(template_id: int, templateArgs: TemplateArgs):

    return {"template name": templateArgs.name, "template id": template_id}

def delete_template(template_id: int):

    return {"template to be deleted: template id": template_id}