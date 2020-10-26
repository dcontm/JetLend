import uuid



def upload_to(instance, filename):
    uuid4 = uuid.uuid4()
    return 'documents/{0}_{1}'.format(uuid4, filename)