#!/bin/bash

# Production script to translate all ClaudeLog documentation to Chinese
# Using the proven approach from testing

echo "========================================="
echo "ClaudeLog Documentation Translation Tool"
echo "========================================="
echo ""

# Configuration
SOURCE_DIR="final-site/docs"
BACKUP_DIR="final-site/docs-backup-$(date +%Y%m%d-%H%M%S)"
LOG_FILE="translation-log-$(date +%Y%m%d-%H%M%S).txt"

# Statistics
TOTAL_FILES=0
SUCCESS_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0

# Files to skip (already in Chinese or special files)
SKIP_FILES=(
    "README.md"
    "index.md"
)

# Function to check if file should be skipped
should_skip() {
    local file="$1"
    for skip in "${SKIP_FILES[@]}"; do
        if [[ "$(basename "$file")" == "$skip" ]]; then
            return 0
        fi
    done
    return 1
}

# Function to translate a single file
translate_file() {
    local file="$1"
    local filename=$(basename "$file")
    
    echo -n "[$((SUCCESS_COUNT + FAILED_COUNT + SKIPPED_COUNT + 1))/$TOTAL_FILES] Translating $filename... "
    
    # Skip if already processed or in skip list
    if should_skip "$file"; then
        echo "SKIPPED"
        ((SKIPPED_COUNT++))
        return
    fi
    
    # Check if already contains Chinese (basic check)
    if grep -q "[\u4e00-\u9fff]" "$file" 2>/dev/null; then
        echo "已翻译 (Already translated)"
        ((SKIPPED_COUNT++))
        return
    fi
    
    # Read file content
    CONTENT=$(cat "$file")
    
    # Create translation prompt
    PROMPT="Please translate this markdown document from English to Chinese.

IMPORTANT RULES:
1. Keep ALL markdown formatting, URLs, code blocks unchanged
2. Translate only natural language text
3. Keep frontmatter unchanged except translate title value
4. Preserve all HTML tags and inline styles
5. Keep technical accuracy
6. For technical terms, use commonly accepted Chinese translations
7. Maintain the same tone as the original

FILE: $filename

$CONTENT

Output ONLY the translated markdown:"
    
    # Translate using Claude CLI
    TRANSLATED=$(claude "$PROMPT" 2>/dev/null)
    
    # Check if translation succeeded
    if [ -n "$TRANSLATED" ] && [ "$TRANSLATED" != "" ]; then
        # Save translated content back to original file
        echo "$TRANSLATED" > "$file"
        echo "✓" | tee -a "$LOG_FILE"
        ((SUCCESS_COUNT++))
    else
        echo "✗ FAILED" | tee -a "$LOG_FILE"
        echo "  Failed: $filename" >> "$LOG_FILE"
        ((FAILED_COUNT++))
    fi
    
    # Small delay to avoid rate limiting
    sleep 2
}

# Main execution
echo "Starting translation process..."
echo "Source directory: $SOURCE_DIR"
echo ""

# Create backup
echo "Creating backup at $BACKUP_DIR..."
cp -r "$SOURCE_DIR" "$BACKUP_DIR"
echo "Backup complete."
echo ""

# Count total files
TOTAL_FILES=$(find "$SOURCE_DIR" -name "*.md" -type f | wc -l | tr -d ' ')
echo "Found $TOTAL_FILES markdown files to process."
echo ""

# Start translation log
echo "Translation Log - $(date)" > "$LOG_FILE"
echo "================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# Process each file
echo "Starting translations..."
echo "================================"

for file in "$SOURCE_DIR"/*.md; do
    if [ -f "$file" ]; then
        translate_file "$file"
    fi
done

# Summary
echo ""
echo "================================"
echo "Translation Summary:"
echo "  Total files: $TOTAL_FILES"
echo "  Translated: $SUCCESS_COUNT"
echo "  Failed: $FAILED_COUNT"
echo "  Skipped: $SKIPPED_COUNT"
echo ""
echo "Backup saved at: $BACKUP_DIR"
echo "Log saved at: $LOG_FILE"
echo ""

# Check if all successful
if [ "$FAILED_COUNT" -eq 0 ]; then
    echo "✓ All translations completed successfully!"
else
    echo "⚠ Some translations failed. Check $LOG_FILE for details."
fi

echo ""
echo "To restore from backup if needed:"
echo "  rm -rf $SOURCE_DIR && mv $BACKUP_DIR $SOURCE_DIR"
echo ""
echo "Translation process complete."