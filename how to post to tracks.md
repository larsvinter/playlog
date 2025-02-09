curl -X POST "https://dw2hys2u3wduxfbyk6sydibsvu0qniac.lambda-url.us-east-1.on.aws" \
     -H "Content-Type: audio/wav" \
     -H "filename: Gareth Emery & Standerwick f. Haliene - Saving Light (Radio Edit).wav" \
     -H "title: Test Song" \
     -H "artist: Test Artist" \
     -H "genre: Electronic" \
     --data-binary "@Gareth Emery & Standerwick f. Haliene - Saving Light (Radio Edit).wav"



     curl -X POST "https://dw2hys2u3wduxfbyk6sydibsvu0qniac.lambda-url.us-east-1.on.aws" \
     -H "Content-Type: application/json" \
     -d '{
           "filename": "Gareth Emery & Standerwick f. Haliene - Saving Light (Radio Edit).wav",
           "contentType": "audio/wav",
           "category": "music",
           "artist": "Gareth Emery",
           "title": "Saving Light",
           "genre": "Electronic"
         }'


     curl -X POST "https://dw2hys2u3wduxfbyk6sydibsvu0qniac.lambda-url.us-east-1.on.aws" \
     -H "Content-Type: application/json" \
     -d '{
           "filename": "If You\'re Waiting For the Commercials - Be Patient - It\'s Gonna Be a While - Copenhagen FM.wav",
           "contentType": "audio/wav",
           "category": "sweeper",
           "producer": "Lars Vinter",
           "speaker": "Chuck Riley"
         }'



{"uploadUrl": "https://radio-items.s3.amazonaws.com/uploads/c8f6b1aa-f7ff-4588-814f-0a0d9de51b94?AWSAccessKeyId=ASIA3WPCOQ73ITVMCR66&Signature=qIlm8%2FR3uk2AbZCf%2FrUr1VvKXzg%3D&content-type=audio%2Fwav&x-amz-security-token=IQoJb3JpZ2luX2VjEGcaCXVzLWVhc3QtMSJGMEQCICuxdY7PNj%2FzorVtZC8eYFJsOF4FfF%2B95UEJX%2Fcw%2Fg4LAiBOnNOlL%2B8lWjrh2fWbZr5VyaUhPjfhJV3hrPWlAolmzCq8AwiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDgwNDE3MDY2MzkyNiIMCKa0NRBTPzdmVMPBKpADLKx1n2eRRymMr2UBRRM7vGOtKXwcowpYxZS9hxmdVPQ6UO3K54ni1Mty%2BHEXs3JlncygW7zpQ4RVB54UMvIiO1%2FQw3VK2YmswZC90Flmj7HFqsi3NKda%2B%2Fra4XHTwPz16AIIEr%2F8Tr9%2BRmIysFkw9xSebNRglQ%2F9Zo9HThD4I7KljvYCQQnLaR%2FCpqACSIeKwqsGHTnx4ZAa4bzkJ1NXObyRIvOwBxeZMHWaAXiv3jE%2B7L6cHsxOozZu%2FMA9zSi6I6hfsT%2BDBStoUNptQpR1EfgHhbRicmtc3E5UFQuj7l6LKCRYvrtvAyQvWHvQ%2FSp7UemeyPvH1GienVAmJ0s1n7NcQl5a3u0eAwWKWx4hJIFpWEtRalzAi5OjEXOIaQyn1Ojb%2BE1SxUvLPZbk%2Be3yjwPnKunhE1LdCLOkDle5%2FzDWuvYpWITIpW75qMS%2BkM147wnaEl1Cqy1qQL60WV1L%2Bc2lNgqq61fDxULpkAekfMVs0FmWwVpHVQP5iWfJwahd4V4e%2F5cacSO8SGdqJty%2FoDDSkZq9BjqfARKjX7zyIleDhGura%2FKSUw1YOQQF7edOyo3y3SdbN2HYqxzRbXlzTi3FwUiN3tBiBhIlVUYzixRrRwrCE%2BBI%2BaxM8Q77YO0IJX64Fsouk5n%2FFHT4byxQtBjNRaLIJIYUmeOVy64eFkkP%2FHCSav1qDTwPyckUsMmPlM7XmdDnd63DueTQ1GLmPPyqS4%2BAvc4OpGWXY0WFjij2OobHUWhn2w%3D%3D&Expires=1738970851", "uploadId": "uploads/c8f6b1aa-f7ff-4588-814f-0a0d9de51b94", "message": "Upload initiated; use the URL to PUT your file."}%  




curl -X PUT "https://radio-items.s3.amazonaws.com/uploads/ea1dd559-bb02-4abe-ac43-db7253f52019.wav?AWSAccessKeyId=ASIA3WPCOQ73CHO5U6CB&Signature=S6CAmnGeCNu4LLyZpxHYw%2FYNbAQ%3D&content-type=audio%2Fwav&x-amz-security-token=IQoJb3JpZ2luX2VjEHkaCXVzLWVhc3QtMSJHMEUCIGq2jm1L1m7IrWM9ZtjGgImxmCmlmUlVLUAmoOSLuPG3AiEAkIC9ImvHCfu%2F8%2BN5cOWy8eB5Kuhwxy8l5IBzl9T7oR0qvAMIkf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw4MDQxNzA2NjM5MjYiDOiltSzRgReHifXRHyqQA%2F%2FU5XFTZSPh1tubmjWOn7o7xKfU4vc2ezXfeWYsSjVwtPh56zwdToSWnTNY8bmkaOgWwMuXXvEZvClJ1DdPrmncUOhSR7LfoJsi%2FwlPPgTn62mgi%2FBb%2BHInFxffbfdOeFxo%2BWfbHqqgCW6uNcso%2FqBg316OYRKcCedKf9gEySS19oGAAKU8f3lyB0IsWvp2T0XDmkdNTLlYkegJUxV%2FHlSlQm%2FVDbvtUvxolR2VCDO3mDx80652985ZuXKlaGeTL6J1OPDwKNcqIZK6JkSKmKsXEcUZLaKptGii2BZLP%2B3VbvINWWrYZUzgT5DAm7CR%2FGKV5QGGZU5M51G5z9goYBTQYv31PM28YH1fCjvHAORgO819CvMny5LR0FRhYUUd5kkjVcWNaqD49Zah3aKZiu8gVEBcg%2F6WW4C0ssktWmL4CjBG8wEvso%2BvI5B%2BKvmHkkTxAKlUTUQZT24xGJB28awG7xpvmmXE2TH3ts2lUvxcJFAWQm1fhAeunf8Hr3MsL8ywzPbJQk9Dofg93LBUELMwiImevQY6ngF%2FyhYbwdzJE2H0u1gxqEO%2FCBgnzw%2B2vKFi08C%2FTME64Y0NrkA5%2FH5pvMiOWGcWcYtOo2erhzoe%2BVRHjp5WoHCNmc0ZSPNPx5hCyhZV1wtAAzsqEx86A418ITHAlMCGa2XLjyrtK4Wm7Oa3Dr6qMKa5TjLtEycilyOMwFgBpVomRnzSs4VHaRCnZLr0rZhk8f6S5q%2BfC6zgyR3M7hTHZQ%3D%3D&Expires=1739035289" \
     -H "Content-Type: audio/wav" \
     --upload-file "If You're Waiting For the Commercials - Be Patient - It's Gonna Be a While - Copenhagen FM.wav"






