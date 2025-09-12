#!/bin/bash

# Fix "See Also" links in mechanics files
cd /Users/ruanchuhao/Downloads/Codes/其他/claudelogTranslate/final-site/docs

# Fix mechanics links
find . -name "mechanics-*.md" -exec perl -pi -e '
    # Fix /mechanics/xxx/ to /mechanics-xxx.html
    s|\(/mechanics/([^/]+)/\)|\(/mechanics-$1.html\)|g;
    
    # Fix /faqs/xxx/ to /faq.html#xxx
    s|\(/faqs/([^/]+)/\)|\(/faq.html#$1\)|g;
    
    # Fix /configuration/ to /configuration.html
    s|\(/configuration/\)|\(/configuration.html\)|g;
    
    # Fix model-comparison link - just remove it as page does not exist
    s|\[模型比较\]\(/model-comparison/\)\||g;
' {} \;

# Also fix similar issues in other files
find . -name "*.md" -exec perl -pi -e '
    # Fix /install-claude-code/ to /install-claude-code.html
    s|\(/install-claude-code/\)|\(/install-claude-code.html\)|g;
    
    # Fix other directory-style links
    s|\(/claude-code-tutorial/\)|\(/claude-code-tutorial.html\)|g;
    s|\(/support-claudelog/\)|\(/support-claudelog.html\)|g;
' {} \;

echo "Links fixed!"