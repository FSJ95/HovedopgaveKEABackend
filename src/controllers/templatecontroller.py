from models.templateargs import TemplateArgs

#TODO: Implement all banner template logic in here including database handling

def get_all_templates():

    return "This should return all templates"

def update_template(template_id: int, templateArgs: TemplateArgs):

    return {"template name": templateArgs.name, "template id": template_id}

def delete_template(template_id: int):

    return {"template to be deleted: template id": template_id}