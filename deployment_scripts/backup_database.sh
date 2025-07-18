#!/bin/bash
set -e
echo "Creating database backup before deployment..."

# Create backup directory if it doesn't exist
mkdir -p /home/ubuntu/db_backups

# Generate timestamp for backup filename
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="/home/ubuntu/db_backups/relay_backup_${TIMESTAMP}.dump"

# Create database backup
echo "Backing up database to: $BACKUP_FILE"
sudo docker exec cce-website-db-1 pg_dump -U webadmin -d relay -Fc > "$BACKUP_FILE"

# Upload to S3 (optional - uncomment if you want automatic S3 backups)
# aws s3 cp "$BACKUP_FILE" s3://ccedbbackup/auto_backups/

# Keep only last 5 backups locally
cd /home/ubuntu/db_backups
ls -t relay_backup_*.dump | tail -n +6 | xargs -r rm

echo "Database backup completed: $BACKUP_FILE" 