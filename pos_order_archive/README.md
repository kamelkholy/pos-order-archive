# POS Order Archive

Archive and unarchive Point of Sale orders in Odoo 19.

## Features

- **Active field** on `pos.order` — enables Odoo's native archive/unarchive mechanism
- **List view** — archived orders appear muted; optional Active column
- **Form view** — red "Archived" ribbon on archived orders
- **Search filter** — dedicated "Archived" filter to find archived orders

## Installation

1. Place the `pos_order_archive` folder in your Odoo custom addons directory
2. Restart the Odoo server
3. Go to **Apps** → **Update Apps List**
4. Search for **"POS Order Archive"** → **Install**

## Usage

1. Navigate to **Point of Sale → Orders → Orders**
2. Select orders → **Action → Archive**
3. To view archived orders: **Filters → Archived**
4. To restore: select archived orders → **Action → Unarchive**

## Compatibility

- Odoo 19.0 Community & Enterprise
- Depends on: `point_of_sale`

## License

LGPL-3 — see [LICENSE](LICENSE) file.
