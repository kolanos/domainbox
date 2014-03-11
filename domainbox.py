from suds.bindings import binding
from suds.client import Client

binding.envns = ('soap12', 'http://www.w3.org/2003/05/soap-envelope')

DOMAINBOX_COMMANDS = {
    'AccountQueryBalance': 'AccountQueryBalanceParameters',
    'AddPublishingAlias': 'AddPublishingAliasParameters',
    'AddWebHostingDatabase': 'AddWebHostingDatabaseParameters',
    'AddWebHostingDatabaseUser': 'AddWebHostingDatabaseUserParameters',
    'AddWebHostingFTPUser': 'AddWebHostingFTPUserParameters',
    'AddWebHostingWebsite': 'AddWebHostingWebsiteParameters',
    'AddWebHostingWebsiteAlias': 'AddWebHostingWebsiteAliasParameters',
    'AddWebHostingWebsiteApp': 'AddWebHostingWebsiteAppParameters',
    'AssignDomain': 'AssignDomainParameters',
    'AssignWebHostingDatabaseUser': 'AssignWebHostingDatabaseUserParameters',
    'AssignWebHostingFTPUser': 'AssignWebHostingFTPUserParameters',
    'CancelBackOrder': 'CancelBackOrderParameters',
    'CancelPremiumDomain': 'CancelPremiumDomainParameters',
    'CancelSSL': 'CancelSSLParameters',
    'CancelTransfer': 'CancelTransferParameters',
    'CancelTransition': 'CancelTransitionParameters',
    'CheckDomainAvailability': 'CheckDomainAvailabilityParameters',
    'CheckDomainAvailabilityBulkQuery':
        'CheckDomainAvailabilityBulkQueryParameters',
    'CheckDomainAvailabilityBulkSubmit':
        'CheckDomainAvailabilityBulkSubmitParameters',
    'CheckDomainAvailabilityPlus': 'CheckDomainAvailabilityPlusParameters',
    'CheckDomainClaims': 'CheckDomainClaimsParameters',
    'CheckDomainValue': 'CheckDomainValueParameters',
    'CheckPremiumDomain': 'CheckPremiumDomainParameters',
    'CheckReportStatus': 'CheckReportStatusParameters',
    'CheckSSLCSR': 'CheckSSLCSRParameters',
    'CheckTLDDocumentation': 'CheckTLDDocumentationParameters',
    'CheckTransferAvailability': 'CheckTransferAvailabilityParameters',
    'CheckTransition': 'CheckTransitionParameters',
    'CompleteTransferAway': 'CompleteTransferAwayParameters',
    'CreateContact': 'CreateContactParameters',
    'CreateDnsRecords': 'CreateDnsRecordsParameters',
    'CreateDnsZone': 'CreateDnsZoneParameters',
    'CreateDomainAuthcode': 'CreateDomainAuthcodeParameters',
    'CreateEmailForwarder': 'CreateEmailForwarderParameters',
    'CreateEmailMailbox': 'CreateEmailMailboxParameters',
    'CreateExternalNameserver': 'CreateExternalNameserverParameters',
    'CreateNameserver': 'CreateNameserverParameters',
    'CreatePublishing': 'CreatePublishingParameters',
    'CreateStorefront': 'CreateStorefrontParameters',
    'CreateSubReseller': 'CreateSubResellerParameters',
    'CreateTrademark': 'CreateTrademarkParameters',
    'CreateUser': 'CreateUserParameters',
    'CreateUserGroup': 'CreateUserGroupParameters',
    'CreateUserRoles': 'CreateUserRolesParameters',
    'CreateWebHosting': 'CreateWebHostingParameters',
    'DeleteContact': 'DeleteContactParameters',
    'DeleteDnsRecords': 'DeleteDnsRecordsParameters',
    'DeleteDnsZone': 'DeleteDnsZoneParameters',
    'DeleteDomain': 'DeleteDomainParameters',
    'DeleteEmail': 'DeleteEmailParameters',
    'DeleteNameserver': 'DeleteNameserverParameters',
    'DeletePublishing': 'DeletePublishingParameters',
    'DeletePublishingAlias': 'DeletePublishingAliasParameters',
    'DeleteTrademark': 'DeleteTrademarkParameters',
    'DeleteUser': 'DeleteUserParameters',
    'DeleteUserGroup': 'DeleteUserGroupParameters',
    'DeleteUserRoles': 'DeleteUserRolesParameters',
    'DeleteWebHostingDatabase': 'DeleteWebHostingDatabaseParameters',
    'DeleteWebHostingDatabaseUser': 'DeleteWebHostingDatabaseUserParameters',
    'DeleteWebHostingFTPUser': 'DeleteWebHostingFTPUserParameters',
    'DeleteWebHostingWebsite': 'DeleteWebHostingWebsiteParameters',
    'DeleteWebHostingWebsiteAlias': 'DeleteWebHostingWebsiteAliasParameters',
    'DeleteWebHostingWebsiteApp': 'DeleteWebHostingWebsiteAppParameters',
    'DisablePublishing': 'DisablePublishingParameters',
    'EnablePublishing': 'EnablePublishingParameters',
    'GetDomainboxContactIds': 'GetDomainboxContactIdsParameters',
    'GetRegistryContactId': 'GetRegistryContactIdParameters',
    'InviteSSL': 'InviteSSLParameters',
    'ListPremiumDomain': 'ListPremiumDomainParameters',
    'ModifyBackOrder': 'ModifyBackOrderParameters',
    'ModifyContact': 'ModifyContactParameters',
    'ModifyDnsRecords': 'ModifyDnsRecordsParameters',
    'ModifyDomainAdditionalData': 'ModifyDomainAdditionalDataParameters',
    'ModifyDomainAuthcode': 'ModifyDomainAuthcodeParameters',
    'ModifyDomainContacts': 'ModifyDomainContactsParameters',
    'ModifyDomainLock': 'ModifyDomainLockParameters',
    'ModifyDomainMemberContact': 'ModifyDomainMemberContactParameters',
    'ModifyDomainNameservers': 'ModifyDomainNameserversParameters',
    'ModifyDomainPrivacy': 'ModifyDomainPrivacyParameters',
    'ModifyDomainProxy': 'ModifyDomainProxyParameters',
    'ModifyDomainRecords': 'ModifyDomainRecordsParameters',
    'ModifyDomainRenewalSettings': 'ModifyDomainRenewalSettingsParameters',
    'ModifyDomainStatus': 'ModifyDomainStatusParameters',
    'ModifyDomainTelCredentials': 'ModifyDomainTelCredentialsParameters',
    'ModifyEmailDomainBlackList': 'ModifyEmailDomainBlackListParameters',
    'ModifyEmailDomainWhiteList': 'ModifyEmailDomainWhiteListParameters',
    'ModifyEmailMailboxAutoResponder':
        'ModifyEmailMailboxAutoResponderParameters',
    'ModifyEmailMailboxBlackList': 'ModifyEmailMailboxBlackListParameters',
    'ModifyEmailMailboxForwarding': 'ModifyEmailMailboxForwardingParameters',
    'ModifyEmailMailboxPassword': 'ModifyEmailMailboxPasswordParameters',
    'ModifyEmailMailboxSpamOption': 'ModifyEmailMailboxSpamOptionParameters',
    'ModifyEmailMailboxWhiteList': 'ModifyEmailMailboxWhiteListParameters',
    'ModifyEmailRenewalSettings': 'ModifyEmailRenewalSettingsParameters',
    'ModifyNameserver': 'ModifyNameserverParameters',
    'ModifyPremiumDomain': 'ModifyPremiumDomainParameters',
    'ModifyPremiumDomainHold': 'ModifyPremiumDomainHoldParameters',
    'ModifyPublishing': 'ModifyPublishingParameters',
    'ModifyPublishingRenewalSettings':
            'ModifyPublishingRenewalSettingsParameters',
    'ModifyResellerConfig': 'ModifyResellerConfigParameters',
    'ModifySSLApproverEmail': 'ModifySSLApproverEmailParameters',
    'ModifySSLSealPreference': 'ModifySSLSealPreferenceParameters',
    'ModifyTrademark': 'ModifyTrademarkParameters',
    'ModifyTransition': 'ModifyTransitionParameters',
    'ModifyUser': 'ModifyUserParameters',
    'ModifyUserGroup': 'ModifyUserGroupParameters',
    'ModifyUserRoles': 'ModifyUserRolesParameters',
    'ModifyWebHosting': 'ModifyWebHostingParameters',
    'ModifyWebHostingFTPUser': 'ModifyWebHostingFTPUserParameters',
    'MsgQueueAcknowledge': 'MsgQueueAcknowledgeParameters',
    'MsgQueueRequest': 'MsgQueueRequestParameters',
    'OrderSSL': 'OrderSSLParameters',
    'ParkingAddDomain': 'ParkingAddDomainParameters',
    'ParkingGetStats': 'ParkingGetStatsParameters',
    'ParkingRemoveDomain': 'ParkingRemoveDomainParameters',
    'PerformAsyncCommands': 'PerformAsyncCommandsParameters',
    'ProcessLaunchDomain': 'ProcessLaunchDomainParameters',
    'PurchasePremiumDomain': 'PurchasePremiumDomainParameters',
    'QueryBackOrder': 'QueryBackOrderParameters',
    'QueryContact': 'QueryContactParameters',
    'QueryDnsRecords': 'QueryDnsRecordsParameters',
    'QueryDnsZone': 'QueryDnsZoneParameters',
    'QueryDomain': 'QueryDomainParameters',
    'QueryDomainAuthcode': 'QueryDomainAuthcodeParameters',
    'QueryDomainContacts': 'QueryDomainContactsParameters',
    'QueryDomainDates': 'QueryDomainDatesParameters',
    'QueryDomainLaunch': 'QueryDomainLaunchParameters',
    'QueryDomainLock': 'QueryDomainLockParameters',
    'QueryDomainMemberContact': 'QueryDomainMemberContactParameters',
    'QueryDomainNameserverHosts': 'QueryDomainNameserverHostsParameters',
    'QueryDomainNameservers': 'QueryDomainNameserversParameters',
    'QueryDomainPrivacy': 'QueryDomainPrivacyParameters',
    'QueryDomainRenewalSettings': 'QueryDomainRenewalSettingsParameters',
    'QueryDomainTelCredentials': 'QueryDomainTelCredentialsParameters',
    'QueryEmailDomainBlackList': 'QueryEmailDomainBlackListParameters',
    'QueryEmailDomainWhiteList': 'QueryEmailDomainWhiteListParameters',
    'QueryEmailForwarder': 'QueryEmailForwarderParameters',
    'QueryEmailMailbox': 'QueryEmailMailboxParameters',
    'QueryEmailMailboxBlackList': 'QueryEmailMailboxBlackListParameters',
    'QueryEmailMailboxWhiteList': 'QueryEmailMailboxWhiteListParameters',
    'QueryFinancialReport': 'QueryFinancialReportParameters',
    'QueryLoginURL': 'QueryLoginURLParameters',
    'QueryManagementReport': 'QueryManagementReportParameters',
    'QueryNameserver': 'QueryNameserverParameters',
    'QueryPerformanceReport': 'QueryPerformanceReportParameters',
    'QueryPremiumDomain': 'QueryPremiumDomainParameters',
    'QueryPublishing': 'QueryPublishingParameters',
    'QueryPublishingControlURL': 'QueryPublishingControlURLParameters',
    'QueryResellerConfig': 'QueryResellerConfigParameters',
    'QuerySSL': 'QuerySSLParameters',
    'QuerySSLApproverEmails': 'QuerySSLApproverEmailsParameters',
    'QuerySSLStatus': 'QuerySSLStatusParameters',
    'QueryTrademark': 'QueryTrademarkParameters',
    'QueryTrademarkLabels': 'QueryTrademarkLabelsParameters',
    'QueryTrademarkSMD': 'QueryTrademarkSMDParameters',
    'QueryTransfer': 'QueryTransferParameters',
    'QueryTransfersAway': 'QueryTransfersAwayParameters',
    'QueryTransition': 'QueryTransitionParameters',
    'QueryUser': 'QueryUserParameters',
    'QueryUserGroup': 'QueryUserGroupParameters',
    'QueryUserRoles': 'QueryUserRolesParameters',
    'QueryWebHosting': 'QueryWebHostingParameters',
    'QueryWebHostingApps': 'QueryWebHostingAppsParameters',
    'QueryWebHostingDatabase': 'QueryWebHostingDatabaseParameters',
    'QueryWebHostingDatabaseUser': 'QueryWebHostingDatabaseUserParameters',
    'QueryWebHostingFTPUser': 'QueryWebHostingFTPUserParameters',
    'QueryWebHostingPackage': 'QueryWebHostingPackageParameters',
    'QueryWebHostingSharedSSL': 'QueryWebHostingSharedSSLParameters',
    'QueryWebHostingUpgrade': 'QueryWebHostingUpgradeParameters',
    'QueryWebHostingWebsite': 'QueryWebHostingWebsiteParameters',
    'QueryWebHostingWebsiteApp': 'QueryWebHostingWebsiteAppParameters',
    'RegisterDomain': 'RegisterDomainParameters',
    'ReissueSSL': 'ReissueSSLParameters',
    'RejectTransferAway': 'RejectTransferAwayParameters',
    'RenewDomain': 'RenewDomainParameters',
    'RenewEmailForwarder': 'RenewEmailForwarderParameters',
    'RenewEmailMailbox': 'RenewEmailMailboxParameters',
    'RenewPublishing': 'RenewPublishingParameters',
    'RenewSSL': 'RenewSSLParameters',
    'RenewWebHosting': 'RenewWebHostingParameters',
    'RequestBackOrder': 'RequestBackOrderParameters',
    'RequestTransfer': 'RequestTransferParameters',
    'RequestTransferAway': 'RequestTransferAwayParameters',
    'ResendDomainVerificationEmail': 'ResendDomainVerificationEmailParameters',
    'ResendSSLEmail': 'ResendSSLEmailParameters',
    'ResendTransferAdminEmail': 'ResendTransferAdminEmailParameters',
    'RestartTransfer': 'RestartTransferParameters',
    'RestartTransition': 'RestartTransitionParameters',
    'RestoreDomain': 'RestoreDomainParameters',
    'ResumeEmail': 'ResumeEmailParameters',
    'StorefrontAssignDomainToUser': 'StorefrontAssignDomainToUserParameters',
    'StorefrontCreatePackage': 'StorefrontCreatePackageParameters',
    'StorefrontCreateUser': 'StorefrontCreateUserParameters',
    'StorefrontDeleteUser': 'StorefrontDeleteUserParameters',
    'StorefrontModifyUser': 'StorefrontModifyUserParameters',
    'StorefrontQueryUser': 'StorefrontQueryUserParameters',
    'StorefrontQueryUsers': 'StorefrontQueryUsersParameters',
    'SuspendEmail': 'SuspendEmailParameters',
    'UnassignWebHostingDatabaseUser':
        'UnassignWebHostingDatabaseUserParameters',
    'UnassignWebHostingFTPUser': 'UnassignWebHostingFTPUserParameters',
    'UnrenewDomain': 'UnrenewDomainParameters',
    'UpgradePublishing': 'UpgradePublishingParameters',
    'UpgradeWebHosting': 'UpgradeWebHostingParameters'
}

LIVE_URL = 'https://live.domainbox.net/?WSDL'
SANDBOX_URL = 'https://sandbox.domainbox.net/?WSDL'


class DomainBox(object):
    def __init__(self, reseller, username, password, live=False):
        url = LIVE_URL if live else SANDBOX_URL

        self.client = Client(url)

        self.factory = self.client.factory
        self.service = self.client.service

        self.auth_params = self.factory.create('AuthenticationParameters')

        self.auth_params.Reseller = reseller
        self.auth_params.Username = username
        self.auth_params.Password = password

    def __getattr__(self, name):
        name = studly_case(name)
        if name in DOMAINBOX_COMMANDS.keys():
            def request_handler(**kwargs):
                return self.request(name, **kwargs)
            return request_handler
        return super(DomainBox, self).__getattr__(name)

    def request(self, name, **kwargs):
        command_params = self.load_command_params(name, **kwargs)
        service = self.service.__getattr__(name)
        return service(self.auth_params, command_params)

    def load_command_params(self, name, **params):
        params_type = self.factory.create(DOMAINBOX_COMMANDS[name])
        for k, v in params.iteritems():
            params_type.__setattr__(studly_case(k), v)
        return params_type


def studly_case(string):
    string = string.replace('ftp', 'FTP')
    return string.replace('_', ' ').title().replace(' ', '')
