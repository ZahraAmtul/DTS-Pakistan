from django.shortcuts import render

def home(request):
    context = {
        'title': 'DTS Lab Pakistan - Leading Digital Solutions',
        'company_name': 'DTS Lab Pakistan',
        'tagline': 'Innovating Digital Transformation Solutions',
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'title': 'About Us - DTS Lab Pakistan',
    }
    return render(request, 'main/about.html', context)

def services(request):
    context = {
        'title': 'Our Services - DTS Lab Pakistan',
        'services': [
            {
                'name': 'Web Development',
                'description': 'Modern, responsive web applications using latest technologies.',
                'icon': '🌐'
            },
            {
                'name': 'Mobile App Development',
                'description': 'Native and cross-platform mobile applications.',
                'icon': '📱'
            },
            {
                'name': 'Digital Transformation',
                'description': 'Complete digital solutions for businesses.',
                'icon': '🚀'
            },
            {
                'name': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and services.',
                'icon': '☁️'
            }
        ]
    }
    return render(request, 'main/services.html', context)

def contact(request):
    context = {
        'title': 'Contact Us - DTS Lab Pakistan',
    }
    return render(request, 'main/contact.html', context)