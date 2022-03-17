import os
import templates
import logging


def lambda_handler(event, context):
    if event['userPoolId'] == os.environ['user_pool_id']:
        if event['triggerSource'] == "CustomMessage_SignUp":
            response = response_email(event, templates.resend_code.RESEND_CODE, "HMV - Bem-vindo")

        if event['triggerSource'] == "CustomMessage_ResendCode":
            response = response_email(event, templates.resend_code.RESEND_CODE, "HMV - Novo código de confirmação")

        if event['triggerSource'] == "CustomMessage_ForgotPassword":
            response = response_email(event, templates.forgot_password.FORGOT_PASSWORD, "HMV - Recuperação de senha")

    return response


def response_email(event, trigger, email_subject):
    event['response']['emailSubject'] = email_subject
    event['response']['emailMessage'] = trigger.format(event['request']['userAttributes']['name'],
                                                       event['request']['codeParameter'])

    logging.info('Email template processed for triggerSource {}'.format(event['triggerSource']))
    return event
