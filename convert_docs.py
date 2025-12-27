
import sys
import re
from pathlib import Path

# CSS for the output HTML to make it look like a professional document
CSS = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #24292e;
        max-width: 850px;
        margin: 0 auto;
        padding: 40px;
    }
    h1, h2, h3 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
    h1 { font-size: 2em; }
    h2 { font-size: 1.5em; margin-top: 24px; }
    h3 { font-size: 1.25em; margin-top: 24px; }
    code {
        padding: 0.2em 0.4em;
        margin: 0;
        font-size: 85%;
        background-color: #f6f8fa;
        border-radius: 3px;
        font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, monospace;
    }
    pre {
        padding: 16px;
        overflow: auto;
        font-size: 85%;
        line-height: 1.45;
        background-color: #f6f8fa;
        border-radius: 3px;
    }
    pre code { background-color: transparent; padding: 0; }
    blockquote {
        padding: 0 1em;
        color: #6a737d;
        border-left: 0.25em solid #dfe2e5;
        margin: 0;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 16px;
    }
    table th, table td {
        padding: 6px 13px;
        border: 1px solid #dfe2e5;
    }
    table tr:nth-child(2n) { background-color: #f6f8fa; }
    @media print {
        body { max-width: none; padding: 0; }
        pre { white-space: pre-wrap; word-wrap: break-word; }
    }
</style>
"""

def simple_markdown_to_html(md_content):
    """
    A lightweight Markdown to HTML converter with regex.
    Used if 'markdown' library is not available.
    """
    html = md_content
    
    # Escape HTML special characters
    html = html.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
    # Headers
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Code blocks (fenced)
    # Note: simplistic handling, doesn't handle nested backticks perfectly
    html = re.sub(r'```(\w+)?\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # Inline code
    html = re.sub(r'`(.*?)`', r'<code>\1</code>', html)
    
    # Bold / Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Lists
    # Simple list handling: replace start of line * or - with <li>
    # Wrap roughly in <ul> (this is a simplified approach)
    lines = html.split('\n')
    in_list = False
    new_lines = []
    for line in lines:
        if line.strip().startswith('* ') or line.strip().startswith('- '):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
            content = line.strip()[2:]
            new_lines.append(f'<li>{content}</li>')
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            new_lines.append(line)
    if in_list:
        new_lines.append('</ul>')
    
    html = '\n'.join(new_lines)
    
    # Paragraphs (simple logic: double newlines = new p)
    # This is tricky with pre-formatted HTML from above, so we skip it for this simple script
    # relying on <br> or just simple line breaks for non-header content usually works okay-ish in simple viewers
    # but let's add simple paragraph wrapping for lines that aren't tags
    
    final_lines = []
    for line in html.split('\n'):
        if not line.strip():
            continue
        if not line.strip().startswith('<'):
            final_lines.append(f'<p>{line}</p>')
        else:
            final_lines.append(line)
            
    return '\n'.join(final_lines)

def convert_to_html():
    input_path = Path(r"C:\Users\Mubashir Khan\.gemini\antigravity\brain\bacc3b8c-93d2-48e3-b107-d2b8693efbbd\codebase_overview.md")
    output_path = input_path.with_suffix('.html')
    
    print(f"Reading from {input_path}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        try:
            import markdown
            print("Using 'markdown' library for conversion...")
            html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
        except ImportError:
            print("'markdown' library not found. Using internal fallback converter...")
            html_content = simple_markdown_to_html(md_content)
            
        full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Codebase Overview</title>
    {CSS}
</head>
<body>
    {html_content}
</body>
</html>
"""
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
            
        print(f"Successfully created: {output_path}")
        print("Done.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_to_html()
