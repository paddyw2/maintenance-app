class backroom:
  def create_backroom(event_id, assigned_id):
    # query
    if(assigned_id == ""):
      optional_values = ""
      license_no = ""
    else:
      optional_values = ", license_no"
      license_no = ", " + str(assigned_id)
    query_string = "insert into backroom(event_id" + optional_values + ") values("+str(event_id) + license_no+");"
    print(query_string)
    return query_string