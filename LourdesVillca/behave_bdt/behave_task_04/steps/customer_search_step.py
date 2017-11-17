from behave import *
from compare import *

from ..utils import utils


@given(u'I send the client name {client_name} to make a Search')
def step_impl(context, client_name):
    context.client_name =client_name
    context.client_id_result = utils.get_client_id(client_name)

@given(u'I send the Client ID {client_id}')
def step_impl(context, client_id):
    context.client_id = int(client_id)
    context.client_name_result = utils.client_list[client_id]

@when(u'I press the "Search" option')
def step_impl(context):
    print("Search Option")

@then(u'I should see the total purchase price {total_price}')
def step_impl(context, total_price):
    expect(utils.price_list(context.client_id)).to_equal(total_price)

