class backroom:
  def create_backroom(event_id, assigned_id):
    # query
    if(assigned_id == ""):
      optional_values = ""
      license_no = ""
    else:
      optional_values = ", assigned_to"
      license_no = ", " + str(assigned_id)
    query_string = "insert into backroom(event_id" + optional_values + ") values("+str(event_id) + license_no+");"
    print(query_string)
    return query_string

  def update_backroom(assigned_id, event_id):
    # query
    if(assigned_id == ""):
      optional_values = ""
      license_no = ""
    else:
      license_no = ", assigned_to=" + str(assigned_id)
    query_string = "update backroom set event_id="+str(event_id) + license_no + " where event_id="+str(event_id)+";"
    print(query_string)
    return query_string
