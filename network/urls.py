from django.conf.urls import patterns, url

from network import views

urlpatterns = patterns('',
                        url(r'^$', views.index, {"retry_message":""}, name='index'),
                        url(r'^NoSample$', views.index, {"retry_message":"No Sample Specified"}, name='indexNoSample'),
                        url(r'^SampleNotFound$', views.index, {"retry_message":"Sample Not Found"}, name='indexSampleNotFound'),
                        url(r'^Ambigous$', views.index, {"retry_message":"Ambigous Alias"}, name='indexAmbigous'),
                        url(r'^network/$', views.network, name='network'),
                        url(r'^pathway/$', views.pathway, name='pathway'),
                        #url(r'^networkWaiting/$', views.networkWaiting, name='networkWaiting'),
                        url(r'^table/$', views.table, name='table'),
                        url(r'^test/$', views.qtests, name='qtests'),
                        url(r'^node_query/$', views.node_query, name='node_query'),
                        url(r'^multi_node_query/$', views.multi_node_query, name='multi_node_query'),
                        url(r'^fullfill_node_query/$', views.fullfill_node_query, name='fullfill_node_query'),
                        url(r'^copy_nodes/$', views.copy_nodes, name='copy_nodes'),
                        url(r'^get_data/$', views.get_data, name='get_data'),
                        url(r'^get_default_parameters/$', views.get_default_parameters, name='get_default_parameters'),
                        url(r'^get_graph/$', views.get_graph, name='get_graph'),
                        url(r'^match_(?P<match_type>\w+)/$', views.get_match, name='get_match'),
                        #url(r'^match_pathway/$', views.match_pathway, name='match_pathway'),
                        #url(r'^match_gene/$', views.match_gene, name='match_gene'),
                        url(r'^get_sample_rels/$', views.get_sample_rels, name='get_sample_rels'),
                        url(r'^save_parameters/$', views.save_parameters, name='save_parameters'),
                        url(r'^load_parameters/$', views.load_parameters, name='load_parameters'),
                        url(r'^password/$', views.password, name='password'),
                        url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'network/login.html', 'extra_context':{'prog_type':views.prog_type, 'username':'Guest'}}),
                        url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': views.prog_type+'/HitWalker2/login/'}))