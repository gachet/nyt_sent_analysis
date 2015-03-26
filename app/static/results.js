var ArticleModel = Backbone.Model.extend({	
	nyt_url: '',
	url: window.location.pathname
});
var articleModel = new ArticleModel();
var Article = Backbone.View.extend({
	el: $("li"),
	events: {
		"click #analysis": "analyze"
	},
	analyze: function(e) {
		var href = $(e.currentTarget).attr("href");
		this.model.set({nyt_url: href});
		this.model.save(null, {
			success: function(model, res) {
				console.log(JSON.parse(res));
			},
			error: function() {
				console.log('REQUEST FAILED');
			}
		});
	}
});
var articleModel = new ArticleModel();
var article = new Article({model: articleModel});