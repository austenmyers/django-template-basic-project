from django.utils import timezone


def get_context():
    try:
        pass
    except Exception as e:
        print(e)
        context = {
            'title': 'New Project',
            'contact': {
                'phone': '208-999-0120',
                'email': 'example@email.com'
            },
            'home_content': 'Example text.',
            'about_us': 'Example text.',
            'locations': [],
        }
    context['site_data'] = {
        'nav': [
            # 'about',
            # 'contact',
        ],
        'developer': 'Austen Myers',
        'year': timezone.now().year,
    }
    return context