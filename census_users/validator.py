from django.core.exceptions import ValidationError
    
def validate_pic_size(value):
    
    if value.size > 2097152:
        raise ValidationError('The maximum file size that can be uploaded is 2MB')