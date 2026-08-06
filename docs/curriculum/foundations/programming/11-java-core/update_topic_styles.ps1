# PowerShell script to update all topic pages with shared CSS
# This replaces inline styles with a link to the shared CSS file

$topicPages = @(
    "01_Basic_Programs\01_Introduction\index.html",
    "01_Basic_Programs\02_Syntax\index.html",
    "01_Basic_Programs\03_Variables\index.html",
    "01_Basic_Programs\04_DataTypes\index.html",
    "01_Basic_Programs\05_Operators\index.html",
    "01_Basic_Programs\06_Input_Output\index.html",
    "02_Conditionals\01_If\index.html",
    "03_Loops\01_While\index.html",
    "05_Arrays\01_Single_Dimensional\index.html",
    "06_Methods\01_WPWR\index.html",
    "07_Strings\01_String_Intro\index.html",
    "08_Regex\01_Character_Classes\index.html",
    "10_OOP\01_Class_and_Object\index.html",
    "11_Collections\01_List\ArrayList\index.html"
)

foreach ($page in $topicPages) {
    $fullPath = "d:\Tech\App\Java_notebook\$page"
    
    if (Test-Path $fullPath) {
        Write-Host "Processing: $page"
        
        # Read the file
        $content = Get-Content $fullPath -Raw
        
        # Calculate the relative path to shared CSS
        $depth = ($page -split '\\').Count - 1
        $relativePath = "../" * $depth + "shared/topic-theme.css"
        
        # Replace the inline <style> block with a link to the shared CSS
        $pattern = '(?s)<style>.*?</style>'
        $replacement = "<link rel=`"stylesheet`" href=`"$relativePath`">"
        
        $newContent = $content -replace $pattern, $replacement
        
        # Write back to file
        Set-Content -Path $fullPath -Value $newContent -NoNewline
        
        Write-Host "Updated: $page" -ForegroundColor Green
    } else {
        Write-Host "File not found: $page" -ForegroundColor Yellow
    }
}

Write-Host "`nAll topic pages have been updated!" -ForegroundColor Cyan
