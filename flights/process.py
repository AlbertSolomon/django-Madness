from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# converting html file to pdf file
def htmlToPdf(templateSource, context_dict = {}):
    template = get_template(templateSource)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1'), result))
    if not pdf.error:
        return HttpResponse(result.getvalue() , content_type ='application/pdf')
    return None

    