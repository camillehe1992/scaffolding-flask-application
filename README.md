# Build a Login Application using Vue3 & Python Flask

Build a login and register application using Vue 3, and Flask. The frontend and backend can interact with each other via API requests/responses.

## Environment & Technical Stacks

### Local Development Environment

| Packages/OS | Version          |
| ----------- | ---------------- |
| PC          | MacBook Air (M2) |
| macOS       | 14.1 (23B74)     |
| Node        | v18.18.2         |
| NPM         | 9.8.1            |
| Python      | Python 3.11.9    |
| Pip         | pip 23.2.1       |
| [Pipenv][1] | 2023.6.12        |

## Technical Stacks

| Technical Skill     | Tool               | Link                                          |
| ------------------- | ------------------ | --------------------------------------------- |
| Frontend Framework  | Vue 3.4.21         | <https://vuejs.org/guide/introduction.html>   |
| Frontend Build Tool | Vite 5.2.0         | <https://vitejs.dev/guide/>                   |
| Frontend UI         | Element Plus 2.7.2 | <https://element-plus.org/en-US/>             |
| Backend Framework   | Flask 3.0          | <https://flask.palletsprojects.com/en/3.0.x/> |

## Get Started

### Frontend

In the `vue-app` component, we use `npm` to manage frontend dependencies.

```bash
cd vue-app
# Install dependencies
npm install
# Start the server
npm run dev
```

The frontend server is running on <http://localhost:5173/>.

### Backend

In the `api` component, we use `pipenv` to manage backend dependencies.

```bash
cd api
# Create a virtualenv at the first time (one-time action)
pipenv install
# Activate virtualenv
pipenv shell
# Install dependencies in Pipfile
pipenv install
# Start server
flask run
```

The Flask server is running on <http://127.0.0.1:5000>.

## References

[1]: https://pipenv.pypa.io/en/latest/index.html
