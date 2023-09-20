from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..notifications import EmailNotification
from ..utils import get_licenses_to_notify

class EmailNotificationAPIView(APIView):
    authentication_classes = []
    def get(self, request):
        licenses_to_notify = get_licenses_to_notify()  # Implement this function to get licenses to notify
        print(licenses_to_notify)
        for license_info in licenses_to_notify:
            recipients = [license_info['poc_email']]
            context = {
                'license_id': license_info['license_id'],
                'license_type': license_info['license_type'],
                'package': license_info['package'],
                'expiration_date': license_info['expiration_date'].strftime('%Y-%m-%d'),
                'poc_name': license_info['poc_name'],
                'poc_email': license_info['poc_email'],
            }
            EmailNotification.send_notification(recipients, context)
            response_data = {
            'detail': 'Email notifications sent',
            'licenses_notified': licenses_to_notify  # Include poc_names in the response
        }
        return Response(response_data, status=status.HTTP_200_OK)