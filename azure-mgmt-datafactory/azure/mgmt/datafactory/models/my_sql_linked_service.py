# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service import LinkedService


class MySqlLinkedService(LinkedService):
    """Linked service for MySQL data source.

    :param connect_via: The integration runtime reference.
    :type connect_via: :class:`IntegrationRuntimeReference
     <azure.mgmt.datafactory.models.IntegrationRuntimeReference>`
    :param description: Linked service description.
    :type description: str
    :param type: Polymorphic Discriminator
    :type type: str
    :param server: Server name for connection. Type: string (or Expression
     with resultType string).
    :type server: object
    :param database: Database name for connection. Type: string (or Expression
     with resultType string).
    :type database: object
    :param schema: Schema name for connection. Type: string (or Expression
     with resultType string).
    :type schema: object
    :param username: Username for authentication. Type: string (or Expression
     with resultType string).
    :type username: object
    :param password: Password for authentication.
    :type password: :class:`SecureString
     <azure.mgmt.datafactory.models.SecureString>`
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'server': {'required': True},
        'database': {'required': True},
    }

    _attribute_map = {
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server': {'key': 'typeProperties.server', 'type': 'object'},
        'database': {'key': 'typeProperties.database', 'type': 'object'},
        'schema': {'key': 'typeProperties.schema', 'type': 'object'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecureString'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, server, database, connect_via=None, description=None, schema=None, username=None, password=None, encrypted_credential=None):
        super(MySqlLinkedService, self).__init__(connect_via=connect_via, description=description)
        self.server = server
        self.database = database
        self.schema = schema
        self.username = username
        self.password = password
        self.encrypted_credential = encrypted_credential
        self.type = 'MySql'
