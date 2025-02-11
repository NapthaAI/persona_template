# Naptha Persona Module Template

This is a base module template for creating personas. You can check out other examples of personas using the CLI commands with the [Naptha SDK](https://github.com/NapthaAI/naptha-sdk). 

### 🛠 Prerequisites 

#### Install Poetry 

From the official poetry [docs](https://python-poetry.org/docs/#installing-with-the-official-installer):

```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/$(whoami)/.local/bin:$PATH"
```

### 🔧 Clone the template and install the Naptha SDK

Clone the repo using:

```bash
git clone https://github.com/NapthaAI/persona-template
cd persona-template
```

You can install the module using:

```bash
poetry install
source .venv/bin/activate
```

You can now use the Naptha CLI. For example, list other examples using:

```bash
naptha personas
```

For each persona, you will see a url where you can check out the data.

### 🔧 Create a New Persona

Change the filename and content of the `data/richard.json` file to create your own persona.

When ready, you can push to your personal GitHub, HuggingFace or IPFS. Make sure to change the remote origin:

```bash
git remote rm origin
git remote add origin https://github.com/persona_name/persona_template.git
```

Also add a new module version number using e.g.:

```bash
git tag v0.1
```

```bash
git push --tags
```

```bash
naptha personas persona_name -p "description='Persona for <persona_name>' parameters='{name: str, bio: List, lore: List, adjectives: List, topics: List, style: Dict[str, List], messageExamples: List, postExamples: List}' module_url='https://github.com/persona_name/persona_template' module_version='v0.1' module_entrypoint='data/richard.json'" 
```

Make sure that the `module_url` is the url of the main repo (e.g the huggingface dataset, github repo, or repo stored on ipfs) and the `module_entrypoint` is the path to the file in the dataset (currently can be json or yaml).

### Delete a Persona

```bash
naptha personas -d persona_name
```

### Run an Agent with a Persona

```bash
naptha run agent:simple_chat_agent -p "tool_name='chat' tool_input_data='who are you?'" --persona_modules "persona_name"
```
