function search(req, res, next) {
  //The user's search term
  var searchTerm = req.query.search;
  //The user's selected category
  var category = req.query.category;

  let query = '';
    if (searchTerm != '' && category != ''){
      query = "SELECT * FROM " + category + "WHERE 'Date' =" + searchTerm;
    }
    else if (searchTerm != '' && category == ''){
      query = "SELECT * FROM " + category + "WHERE 'Date' =" + searchTerm;
    }
    else if (searchTerm == '' && category != ''){
      query = "SELECT * FROM " + category + "WHERE 'Date' =" + searchTerm;
    }

    database.query(query, (err, result) => {
      if (err) {
        req.searchResult="";
        req.searchTerm="";
        req.category="";
        next();
      }

    req.searchResult = result;
    req.searchTerm = searchTerm;
    req.category = "";

    next();
    
  });}

app.get('/example,', search, (req, res) => {
  var searchResult = req.searchResult
  res.render('pages/example', {
    results: searchResult.Length,
    searchTerm: req.searchTerm,
    searchResult: searchResult,
    category: req.category
  });
})