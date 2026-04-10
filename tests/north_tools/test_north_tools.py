def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_plugin_fitness.north_tools import north_entry_point

    expected_id = 'nomad-plugin-fitness-my-north-tool'
    assert (
        north_entry_point.id_url_safe == expected_id
        or north_entry_point.id == 'nomad-north-nomad-plugin-fitness'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'
