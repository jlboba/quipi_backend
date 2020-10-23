# quipi_backend

### Endpoints 

- `/api/prompts` gets all prompts and their corresponding quips 
- `/api/prompts/:id` gets a particular prompt and their corresponding quips
- `/api/quips` gets all quips and the corresponding prompt text
- `/api/quips/:id` gets a particular quip and their corresponding prompt text

### Filtering 

Both models can be filtered using the following query parameters 

#### `playable` 

- accepts values `true` or `false`

Example 

> `/api/prompts?playable=true`
