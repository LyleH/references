#This is a hack for seller portal
#Replace the function submit_po with this code

def submit_po(shipment_id, request):
    shipment = marketplace.get_shipment(shipment_id)[0]
    if not marketplace.get_units_in_shipment(shipment_id)['units']:
        return mark_as_closed(shipment_id)
    instruction_id = None if not shipment['idInstruction'] else shipment['idInstruction']
    eta_max = tal.core.util.add_work_days(datetime.datetime.now(), 2)
    shipment_items = marketplace.get_shipment_items({'shipment_id': shipment_id})
    instruction_items = []
    for shipment_item in shipment_items:
        if shipment_item['Status'] == ShipmentState.IN_PROGRESS and shipment_item['QtyShipped'] > 0:
            instruction_items.append({
                'product': shipment_item['idSellerListing'],
                'qty': shipment_item['QtyShipped'],
                'cost_price': shipment_item['CostPrice'],
                'date_paid': shipment_item['DatePaid'],
                'eta_max': eta_max.strftime("%Y-%m-%d")
            })
    if instruction_items and not instruction_id:
        data = {
            'warehouse': shipment['idWarehouse'],
            'seller': shipment['idSupplier'],
            'comments': 'Marketplace',
            'is_manual': 1,
            'id_customer': request.user.idcustomer,
            'ETAMax': eta_max.strftime("%Y-%m-%d"),
            'items': instruction_items
        }
        '''
        # Create purchase order
        result = wms_client.post_purchaseorder_create(data)
        if result and result['instruction'] and len(result['items_added']) > 0:
            instruction_id = result['instruction']['id']
            if len(result['items_failed']) > 0:
                raise ValueError("Purchase Order %s successfully created but some items failed to be added." \
                                 % result['instruction']['id'])
        else:
            raise ValueError("Purchase Order could not be created.")
        '''
    instruction_id = 1
    if instruction_id:
        doc = {
            'shipment_id': shipment_id,
            'shipment_status_id': ShipmentState.CONFIRMED,
            'instruction_id': instruction_id,
            'date_submitted': datetime.datetime.now(),
            'date_ready_to_ship': datetime.datetime.now(),
            'date_estimated_arrival': eta_max.strftime("%d-%m-%Y")
        }
        marketplace.update_shipment(doc)
        for shipment_item in shipment_items:
            if shipment_item['QtyInProgress']:
                doc = {
                    'shipment_item_id': shipment_item['idShipmentItem'],
                    'status': ShipmentState.CONFIRMED
                }
                marketplace.update_shipment_item(doc)
            else:
                marketplace.delete_shipment_item(shipment_item['idShipmentItem'])
        # Submit purchase order
        '''
        send_response = wms_client.get_purchaseorder_submit(instruction_id)
        if send_response:
            if send_response.get('result') == "failure":
                logger.error('WMS error: %s' % repr(send_response.get('errors')))
                raise ValueError('There was an error sending data to the warehouse')
            elif send_response.get('result') != "success":
                logger.error('WMS error unknown response: %s' % repr(send_response))
                raise ValueError('There was an unexpected error sending data to the warehouse.')
        else:
            logger.error('WMS error unknown response: %s' % repr(send_response))
            raise ValueError('There was an unexpected error sending data to the warehouse.')
        '''
    else:
        raise ValueError('There was an unexpected error creating the Purchase Order')