# Odoo 17 Development Environment

## Prerequisites

- [Docker](https://www.docker.com/get-started) and Docker Compose installed

## Quick Start

### 1. Start the environment

```bash
docker compose up -d
```

### 2. Access Odoo

- Open **http://localhost:8069** in your browser
- On first launch you'll see the database creation screen:
  - **Master Password**: leave default or set one
  - **Database Name**: choose a name (e.g. `odoo-dev`)
  - **Email / Password**: set your admin credentials
  - **Language / Country**: pick yours
  - Check **Demo data** if you want sample data

### 3. Install your custom module

1. Go to **Apps**
2. Click **Update Apps List** (you may need to enable Developer Mode first)
3. Search for **"My Custom Module"**
4. Click **Install**

## Project Structure

```
.
├── docker-compose.yml          # Docker services (Odoo + PostgreSQL)
├── config/
│   └── odoo.conf               # Odoo server configuration
├── custom-addons/              # Your custom modules go here
│   └── my_custom_module/       # Sample module
│       ├── __manifest__.py     # Module metadata
│       ├── __init__.py         # Python package init
│       ├── models/             # Business logic (models)
│       ├── views/              # UI definitions (XML)
│       └── security/           # Access control
└── README.md
```

## Development Workflow

### Enable Developer Mode

Go to **Settings** → scroll to bottom → click **Activate the developer mode**

Or navigate to: `http://localhost:8069/web?debug=1`

### Create a new module

1. Create a new folder under `custom-addons/`:
   ```
   custom-addons/
   └── your_module_name/
       ├── __manifest__.py
       ├── __init__.py
       ├── models/
       │   ├── __init__.py
       │   └── your_model.py
       ├── views/
       │   └── your_views.xml
       └── security/
           └── ir.model.access.csv
   ```

2. Restart Odoo to pick up the new module:
   ```bash
   docker compose restart odoo
   ```

3. In the browser: **Apps** → **Update Apps List** → search & install

### Auto-reload (dev mode)

The config has `dev_mode = reload,xml` enabled, which means:
- **Python changes** trigger an automatic server reload
- **XML view changes** are reloaded without restarting

### View logs

```bash
docker compose logs -f odoo
```

### Stop the environment

```bash
docker compose down
```

### Reset everything (destroy database & filestore)

```bash
docker compose down -v
```

## Common Commands

| Command | Description |
|---------|-------------|
| `docker compose up -d` | Start services in background |
| `docker compose down` | Stop services |
| `docker compose down -v` | Stop and remove volumes (reset all data) |
| `docker compose restart odoo` | Restart Odoo (pick up new modules) |
| `docker compose logs -f odoo` | Tail Odoo logs |
| `docker compose exec odoo bash` | Shell into the Odoo container |

## Useful Resources

- [Odoo 17 Developer Documentation](https://www.odoo.com/documentation/17.0/developer.html)
- [OWL (Odoo Web Library)](https://www.odoo.com/documentation/17.0/developer/reference/frontend/owl.html)
- [Odoo ORM API](https://www.odoo.com/documentation/17.0/developer/reference/backend/orm.html)
