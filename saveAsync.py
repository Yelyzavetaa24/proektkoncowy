async def load_and_save_data_async(input_file, output_file):
    loop = asyncio.get_event_loop()
    json_data = await loop.run_in_executor(None, load_json_data, input_file)
    if json_data:
        await loop.run_in_executor(None, save_json_data, json_data, output_file)

    yaml_data = await loop.run_in_executor(None, load_yaml_data, input_file)
    if yaml_data:
        await loop.run_in_executor(None, save_yaml_data, yaml_data, output_file)

    xml_data = await loop.run_in_executor(None, load_xml_data, input_file)
    if xml_data:
        await loop.run_in_executor(None, save_xml_data, xml_data, output_file)
