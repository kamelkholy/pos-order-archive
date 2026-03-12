# Odoo 19 Development Environment

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

### 3. Install the POS Order Archive module

1. Go to **Apps**
2. Click **Update Apps List** (enable Developer Mode first if needed)
3. Search for **"POS Order Archive"**
4. Click **Install**

## Project Structure

```
.
├── docker-compose.yml              # Docker services (Odoo 19 + PostgreSQL 16)
├── config/
│   └── odoo.conf                   # Odoo server configuration
├── pos_order_archive/              # Custom module (mounted as addon)
│   ├── __manifest__.py
│   ├── __init__.py
│   ├── models/
│   │   └── pos_order.py            # Adds active field to pos.order
│   ├── views/
│   │   └── pos_order_views.xml     # List, form, search view extensions
│   ├── static/
│   │   └── description/            # App store assets
│   ├── LICENSE
│   └── README.md
└── README.md
```

## Development Workflow

### Enable Developer Mode

Go to **Settings** → scroll to bottom → click **Activate the developer mode**

Or navigate to: `http://localhost:8069/web?debug=1`

### Create a new module

1. Create a new folder at the repo root:
   ```
   your_module_name/
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

2. Add the volume mount in `docker-compose.yml`:
   ```yaml
   - ./your_module_name:/mnt/extra-addons/your_module_name
   ```

3. Restart Odoo to pick up the new module:
   ```bash
   docker compose restart odoo
   ```

4. In the browser: **Apps** → **Update Apps List** → search & install

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

- [Odoo 19 Developer Documentation](https://www.odoo.com/documentation/19.0/developer.html)
- [OWL (Odoo Web Library)](https://www.odoo.com/documentation/19.0/developer/reference/frontend/owl.html)
- [Odoo ORM API](https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html)
