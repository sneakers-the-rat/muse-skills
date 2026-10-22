### Loading Tools

Tools are organized into namespaces and functions. Some namespaces are not loaded fully and need to be loaded. Call `tool_search.load_tool_namespace` with the namespace's name to get its deferred function descriptions and parameter schemas. While a tool's schema is in your context, you can use it without loading it again.

- Namespaces marked "{deferred_stub_marker}" have deferred functions. A namespace whose functions are all deferred hides their entries until loaded.
- Namespaces marked "{deferred_function_marker}" have no parameter schema for the functions until loaded.
- Namespaces with fully specified functions and schemas are not deferred and can be called directly.

