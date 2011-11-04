
// Load the application once the DOM is ready, using `jQuery.ready`:
$(function(){

    window.Blastdb = Backbone.Model.extend({

	//the url of this model. Overridden to add a slash at the end.
	url : function() {
	    var base = this.collection.url;
	    if (this.isNew()) return base;
	    return base + (base.charAt(base.length - 1) == '/' ? '' : '/') + this.id + '/';
	}
	
    });

  window.Blastdbs = Backbone.Collection.extend({

      // Reference to this collection's model.
      model: Blastdb,
      url  : '/api/blastdb/',

      //called with the attributes of a DB, will either add a newly created model (NOT sync with the server)
      //or update a model that already exists. This is used to update the view after creating or updating a model
      //
      //We need to do the create/upload awkwardly outside of backbone because it involves uploading files
      addOrUpdate: function(data)
      {
	  if (model = this.get(data.id)) model.set(data);
	  else this.add(data);
      }
  });

  window.DBs = new Blastdbs;

  //the View
  // The DOM element for a DB item...
  // --------------------------------
  window.DBView = Backbone.View.extend({

    tagName:  "tr",

    // Cache the template function for a single item.
    template: _.template($('#DB-template').html()),


      //I'm sure this could be simpler but it works. I'm trying to call a function in the context
      //of the view when the model's event fires.
      _remove: function(a){
	  return function(){a.remove()};
      },
   
    initialize: function() {
      //_.bindAll(this, 'render', 'close');
	//this.model.bind('change', this.render);
	this.model.bind('remove', this._remove(this))
	this.model.view = this;
    },

    // Re-render the contents of the todo item.
    render: function() {
      $(this.el).html(this.template(this.model.toJSON()));
      //this.setContent();
      return this;
    },

    clear: function() {
      this.model.clear();
    }

  });

  // The Application
  // ---------------

  // Our overall **AppView** is the top-level piece of UI.
  window.AppView = Backbone.View.extend({

    el: $("#DB-list"),

    // At initialization we bind to the relevant events on the 
    // collection, when items are added or changed. Kick things off by
    // loading any preexisting todos that might be saved in *localStorage*.
    initialize: function() {
      _.bindAll(this, 'addOne', 'addAll', 'render');


      DBs.bind('add',     this.addOne);
      DBs.bind('refresh', this.addAll);
      DBs.bind('all',     this.render);

      DBs.fetch();
    },

    render: function() {
	DBs.each(function(db){db.view.render()});
    },

    // Add a single item to the list by creating a view for it, and
    // appending its element to the table
    addOne: function(db) {
      var view = new DBView({model: db});
      $("#DB-list").append(view.render().el);
    },

    // Add all items in the collection at once.
    addAll: function() {
      DBs.each(this.addOne);
    },





  });

  // Finally, we kick things off by creating the App.
  window.App = new AppView;

});

//this is part of the workaround to achieve asynchronous CRUD on a resource whose C and U involve a file upload.
//the argument of uploadDone is the frame to which the server response from the POST request is targeted (see blastdb.tmpl)
//It is assumed to have JSON in its body.
function uploadDone(frame) { //Function will be called when iframe is loaded.
       var ret = frame.contentDocument.body.innerHTML;
        try{
            if( ret != ""){
               var data = JSON.parse(ret);
                if(data.response == "OK") { 
                    alert('uploaded');
		    window.DBs.addOrUpdate(data)
               }
               else { //Upload failed - show user the reason.
                   alert("Blast DB creation failed: "+data.exception);
               }
            } 
        } catch(err){
            alert('upload failed: '+err.extMessage+err.stack)
        }
}

