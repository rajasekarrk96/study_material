# PowerShell script to add Practice Worksheets button to all module index.html files

# Find all index.html files in subdirectories (excluding the main index.html)
$files = Get-ChildItem -Path "d:\Tech\App\Java_notebook" -Recurse -Filter "index.html" | Where-Object { 
    $_.FullName -ne "d:\Tech\App\Java_notebook\index.html" -and
    $_.FullName -notlike "*\shared\*"
}

$count = 0
$updated = 0
$skipped = 0

foreach ($file in $files) {
    $count++
    $relativePath = $file.FullName.Replace("d:\Tech\App\Java_notebook\", "")
    Write-Host "`n[$count] Processing: $relativePath" -ForegroundColor Cyan
    
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    
    # Check if button already exists
    if ($content -match "Practice Worksheets") {
        Write-Host "  Already has Practice Worksheets button - Skipping" -ForegroundColor Yellow
        $skipped++
        continue
    }
    
    # Find the pattern: Back to Home link followed by <hr>
    $pattern = '(<a href="[^"]*index\.html#[^"]*">← Back to Home</a>)\s*(<hr[^>]*>)'
    
    if ($content -match $pattern) {
        # Create the button HTML
        $buttonHtml = '        <a href="worksheet.html" class="btn btn-primary" style="display: block; margin: 10px 0; padding: 10px; text-align: center; background-color: #dc3545; color: white; text-decoration: none; border-radius: 5px; font-weight: 600;">' + "`r`n" + '            📝 Practice Worksheets' + "`r`n" + '        </a>' + "`r`n" + '        <hr style="border-color: #34495e; margin: 15px 0;">'
        
        # Replace the pattern
        $replacement = '$1' + "`r`n" + $buttonHtml
        $newContent = $content -replace $pattern, $replacement
        
        # Write back to file
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8 -NoNewline
        Write-Host "  Successfully added Practice Worksheets button" -ForegroundColor Green
        $updated++
    }
    else {
        Write-Host "  Pattern not found - manual review needed" -ForegroundColor Red
    }
}

Write-Host "`n=================================================="
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Total files processed: $count"
Write-Host "  Successfully updated: $updated" -ForegroundColor Green
Write-Host "  Already had button: $skipped" -ForegroundColor Yellow
Write-Host "==================================================`n"
