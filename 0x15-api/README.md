
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="google" content="notranslate">

      <script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({"userId":306856,"visitorType":"student","batch":{"id":95,"fullNameWithC":"KGL-0423 (C#15)","schoolLocation":{"id":6,"name":"Kigali"}},"curriculum":{"id":1,"name":"SE Foundations"}});

    window.gtm_user_custom_event = function (name, options) {
      if (typeof name === 'undefined') {
        return;
      }

      window.dataLayer.push({
        customEventOptions: typeof options !== 'undefined' ? options : {},
        event: name,
      });
    }
  </script>

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-N4C8MF2');</script>
  <!-- End Google Tag Manager -->


    <title>Project: 0x15. API | Kigali Intranet</title>

      <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
      <link rel="stylesheet" media="all" href="/assets/application_alx-8941610700856adf24a6e389e4f744b0cefa6db7b3bc8157ea63b16ddcf11590.css" />
      <script src="https://www.gstatic.com/charts/loader.js"></script>
      <script src="/assets/application-e108fb75f939d72d47f0e99c7163aee8c5572427c1e62e5b50334df42d03f2d3.js"></script>
      <link rel="shortcut icon" type="image/x-icon" href="/favicon_alx.ico" />
      <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="FWiqVLZimF2ssKY_ZnciNRD8HcByVi_atzFbBfza7BhiekdkrMzTS2jBG6eCm1DxN2UvGkN7FBEZ33yQ3J_U2A" />

      <link rel="apple-touch-icon" href="/apple-touch-icon_alx.png">

      <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
      <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
      <![endif]-->

      <!-- Store user timezone -->
      <script>
        Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
      </script>

      <!-- intro.js for interactive onboarding -->

      <!-- React -->
      <script src="/packs/js/application-5e52ac700b37dc1d7140.js"></script>
      <link rel="stylesheet" media="screen" href="/packs/css/application-87456da7.css" />
  </head>

  <body class="signed_in env_production notranslate"
        translate="no"
        class="notranslate"
        data-theme-suffix="_alx">
      <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N4C8MF2"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->


      <input type="hidden" id="hbtn-slack-url" value="https://alx-students.slack.com">
      <nav class="navbar navbar-default navbar-fixed-top topbar visible-xs">
  <div class="navbar-header">
    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-mobile" aria-expanded="false">
      <span class="sr-only">Toggle navigation</span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
      <span class="icon-bar"></span>
    </button>

    <a class="navbar-brand" href="/">
      <div class="logo"></div>
</a>  </div>

  <div class="collapse navbar-collapse navigation" id="navbar-mobile">
    <ul class="nav navbar-nav">
      


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My Planning"><a href="/planning/me"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar "></i></div><div class="visible-xs">My Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa-solid fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa-solid fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa-solid fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>


<hr class="visible-xs">

<li>

      <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Discord">
        <a rel="noreferrer" target="_blank" href="https://discord.com/app">
          <div class="icon discord">
            <i aria-hidden="true" class="fa-brands fa-discord "></i>
          </div>
          <div class="visible-xs">Discord</div>
</a>      </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.amazonaws.com/alx-intranet.hbtn.io/users/photos/000/306/856/thumb/DSC_9334.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240104%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240104T003226Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e0071f30b849b62ff49c5bd1867e73559eda49515136ed111544dc05585e32cd')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


    </ul>
  </div>
</nav>

      <div class="hidden-xs navigation sidebar">
  <a class="logo-container" href="/">
    <div class="logo"></div>
</a>
  <ul>
    


    <li data-container="body" data-placement="right" data-toggle="tooltip" title="My Planning"><a href="/planning/me"><div class="icon "><i aria-hidden="true" class="fa-solid fa-calendar "></i></div><div class="visible-xs">My Planning</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-current-projects-item" title="Projects"><a href="/projects/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-code-fork "></i></div><div class="visible-xs">Projects</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="QA Reviews I can make"><a href="/corrections/to_review"><div class="icon "><i aria-hidden="true" class="fa-solid fa-check "></i></div><div class="visible-xs">QA Reviews I can make</div></a></li>
    
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Evaluation quizzes"><a href="/dashboards/my_current_evaluation_quizzes"><div class="icon "><i aria-hidden="true" class="fa-solid fa-question "></i></div><div class="visible-xs">Evaluation quizzes</div></a></li>

    <hr title="My resources">

    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Curriculums"><a href="/dashboards/my_curriculums"><div class="icon "><i aria-hidden="true" class="fa-solid fa-graduation-cap "></i></div><div class="visible-xs">Curriculums</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-concepts-item" title="Concepts"><a href="/concepts"><div class="icon "><i aria-hidden="true" class="fa-solid fa-file-text "></i></div><div class="visible-xs">Concepts</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-video-rooms" title="Conference rooms"><a href="/dashboards/video_rooms"><div class="icon "><i aria-hidden="true" class="fa-solid fa-comments "></i></div><div class="visible-xs">Conference rooms</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Servers"><a href="/servers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-server "></i></div><div class="visible-xs">Servers</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" id="sidebar-dashboards-my-containers" title="Sandboxes"><a href="/user_containers/current"><div class="icon "><i aria-hidden="true" class="fa-solid fa-terminal "></i></div><div class="visible-xs">Sandboxes</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Tools"><a href="/dashboards/my_tools"><div class="icon "><i aria-hidden="true" class="fa-solid fa-wrench "></i></div><div class="visible-xs">Tools</div></a></li>
    <li data-container="body" data-placement="right" data-toggle="tooltip" title="Video on demand"><a href="/dashboards/videos"><div class="icon "><i aria-hidden="true" class="fa-solid fa-film "></i></div><div class="visible-xs">Video on demand</div></a></li>

      <hr title="My campus">

      
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Peers"><a href="/users/peers"><div class="icon "><i aria-hidden="true" class="fa-solid fa-users "></i></div><div class="visible-xs">Peers</div></a></li>
      <li data-container="body" data-placement="right" data-toggle="tooltip" title="Captain&#39;s Logs"><a href="/dashboards/my_captain_log"><div class="icon "><i aria-hidden="true" class="fa-solid fa-book "></i></div><div class="visible-xs">Captain&#39;s Logs</div></a></li>


<hr class="visible-xs">

<li>

      <div
      data-container="body"
      data-placement="right"
      data-toggle="tooltip"
      title="Discord">
        <a rel="noreferrer" target="_blank" href="https://discord.com/app">
          <div class="icon discord">
            <i aria-hidden="true" class="fa-brands fa-discord "></i>
          </div>
          <div class="visible-xs">Discord</div>
</a>      </div>

  <div
    data-container="body"
    data-placement="right"
    data-toggle="tooltip"
    title="My Profile">
    <a href="/users/my_profile">
        <div class="image ">
          <div class="inner" style="background-image: url('https://s3.amazonaws.com/alx-intranet.hbtn.io/users/photos/000/306/856/thumb/DSC_9334.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240104%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20240104T003226Z&amp;X-Amz-Expires=600&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=e0071f30b849b62ff49c5bd1867e73559eda49515136ed111544dc05585e32cd')"></div>
        </div>

      <div class="visible-xs">My Profile</div>
</a>  </div>
</li>


  </ul>
</div>


    <main>
        <div id="layout-bars">
          
          
          
          
          
          
        </div>

      <article class="">

        
<div class="project row">
  <div class="col-xs-12 col-md-10 col-lg-8 contains-images">

      <h1 class="gap">0x15. API</h1>

  <div data-react-class="tags/Tags" data-react-props="{&quot;tags&quot;:[{&quot;id&quot;:19,&quot;value&quot;:&quot;Python&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:28,&quot;value&quot;:&quot;Scripting&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:35,&quot;value&quot;:&quot;Back-end&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;},{&quot;id&quot;:36,&quot;value&quot;:&quot;API&quot;,&quot;author_id&quot;:null,&quot;created_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;,&quot;updated_at&quot;:&quot;2022-06-16T01:59:38.000Z&quot;}]}" data-react-cache-id="tags/Tags-0"></div>

  <div data-react-class="projects/ProjectMetadata" data-react-props="{&quot;metadata&quot;:{&quot;author&quot;:&quot;Sylvain Kalache, co-founder at Holberton School&quot;,&quot;weight&quot;:1,&quot;correction&quot;:{&quot;released&quot;:true,&quot;auto_correction_available_at&quot;:&quot;2024-01-03T12:00:00.000+02:00&quot;,&quot;requires_auto_correction&quot;:true,&quot;requires_manual_correction&quot;:false},&quot;bpi&quot;:{&quot;current&quot;:true,&quot;started&quot;:false,&quot;in_second_deadline&quot;:false,&quot;starts_at&quot;:&quot;2024-01-03T06:00:00.000+02:00&quot;,&quot;ends_at&quot;:&quot;2024-01-04T06:00:00.000+02:00&quot;,&quot;second_deadline_at&quot;:&quot;2024-01-06T06:00:00.000+02:00&quot;}}}" data-react-cache-id="projects/ProjectMetadata-0"></div>




    


    <div id="project_id" style="display: none" data-project-id="269"></div>



      

      

      <div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Background Context</h2>

<p><a href="https://youtu.be/-2kyU6-j8ZQ" target="_blank"><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240104T003226Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4352c6caf45d251221f69fb3005941702a7f5e07348bc377bde320a14f1a52dc" alt="" loading='lazy' style="" /></a></p>

<p>Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.</p>

<p>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them &ndash; access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.</p>

<p>This is a perfect example of a task that is not suited for Bash scripting, so let&rsquo;s build Python scripts.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/KMFzqRAqedMf7AHHBD_43g" title="Friends don&#39;t let friends program in shell script" target="_blank">Friends don&rsquo;t let friends program in shell script</a> </li>
<li><a href="/rltoken/zeBO6_RNTlwaotyRRNAzoQ" title="What is an API" target="_blank">What is an API</a> </li>
<li><a href="/rltoken/bf09Qp6QY44CANLzxxRbPA" title="What is an API? In English, please" target="_blank">What is an API? In English, please</a></li>
<li><a href="/rltoken/fA164QWEnZxaSngBD3EPRQ" title="What is a REST API" target="_blank">What is a REST API</a> </li>
<li><a href="/rltoken/n4h77IbBuDxTE3bhes_AyQ" title="What are microservices" target="_blank">What are microservices</a> </li>
<li><a href="/rltoken/b7V1ROY6kSRxDDKnsJoqxg" title="PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry" target="_blank">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/03Evn5VsICwJUAiTdu0zHA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What Bash scripting should not be used for</li>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV format</li>
<li>What is the JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class name style</li>
<li>Pythonic Variable name style</li>
<li>Pythonic Function name style</li>
<li>Pythonic Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>
</ul>

<h3>Copyright - Plagiarism</h3>

<ul>
<li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
<li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work. </li>
<li>You are not allowed to publish any content of this project.</li>
<li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li><strong>Libraries imported in your Python files must be organized in alphabetical order</strong></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>You must use <a href="/rltoken/CNqOWPW6mdYuK7Ak-f2KHQ" title="get" target="_blank">get</a> to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
<li>Your code should not be executed when imported (by using <code>if __name__ == &quot;__main__&quot;:</code>)</li>
</ul>

  </div>
</div>


      

      

        
          <h2 class="gap">Tasks</h2>

    <div data-role="task1732" data-position="1" id="task-num-0">
      <div class="panel panel-default task-card " id="task-1732">
  <span id="user_id" data-id="306856"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Gather data from an API
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="306856"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Write a Python script that, using this <a href="/rltoken/7cr7aLYdaWAZWBKrBKS12A" title="REST API" target="_blank">REST API</a>, for a given employee ID, returns information about his/her TODO list progress.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>urllib</code> or <code>requests</code> module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress in this exact format:

<ul>
<li>First line: <code>Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):</code>

<ul>
<li><code>EMPLOYEE_NAME</code>: name of the employee</li>
<li><code>NUMBER_OF_DONE_TASKS</code>: number of completed tasks</li>
<li><code>TOTAL_NUMBER_OF_TASKS</code>: total number of tasks, which is the sum of completed and non-completed tasks</li>
</ul></li>
<li>Second and N next lines display the title of completed tasks: <code>TASK_TITLE</code> (with 1 tabulation and 1 space before the <code>TASK_TITLE</code>)</li>
</ul></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     aliquam aut quasi
     veritatis pariatur delectus
     nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis
     repellendus veritatis molestias dicta incidunt
     excepturi deleniti adipisci voluptatem et neque optio illum ad
     totam atque quo nesciunt
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
sylvain@ubuntu$
sylvain@ubuntu$ python3 0-gather_data_from_an_API.py 4 | tr &quot; &quot; &quot;S&quot; | tr &quot;\t&quot; &quot;T&quot; 
EmployeeSPatriciaSLebsackSisSdoneSwithStasks(6/20):
TSoditSoptioSomnisSquiSsunt
TSdoloremqueSautSdoloresSquidemSfugaSquiSnulla
TSsintSametSquiaStotamScorporisSquiSexercitationemScommodi
TSsequiSdoloremSsed
TSeumSipsaSmaximeSut
TStemporeSmolestiasSdoloresSrerumSsequiSvoluptatesSipsumSconsequatur
sylvain@ubuntu$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x15-api</code></li>
            <li>File: <code>0-gather_data_from_an_API.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1732">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1732" data-batch-id="95" data-toggle="modal" data-target="#task-1732-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-1732-users-done-modal" data-task-id="1732" data-batch-id="95">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "0. Gather data from an API"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm check-your-task-1732-modal-button" data-task-id="1732" data-toggle="modal" data-target="#task-test-correction-1732-correction-modal" id="task-num-0-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:1732}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1732-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "0. Gather data from an API"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1732">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1732">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="1732">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1732}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1733" data-position="2" id="task-num-1">
      <div class="panel panel-default task-card " id="task-1733">
  <span id="user_id" data-id="306856"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      1. Export to CSV
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="306856"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Using what you did in the task #0, extend your Python script to export data in the CSV format.</p>

<p>Requirements:</p>

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>&quot;USER_ID&quot;,&quot;USERNAME&quot;,&quot;TASK_COMPLETED_STATUS&quot;,&quot;TASK_TITLE&quot;</code></li>
<li>File name must be: <code>USER_ID.csv</code></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;suscipit repellat esse quibusdam voluptatem incidunt&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;distinctio vitae autem nihil ut molestias quo&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;et itaque necessitatibus maxime molestiae qui quas velit&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;adipisci non ad dicta qui amet quaerat doloribus ea&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;voluptas quo tenetur perspiciatis explicabo natus&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;aliquam aut quasi&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;veritatis pariatur delectus&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;nesciunt totam sit blanditiis sit&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;laborum aut in quam&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;repudiandae totam in est sint facere fuga&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;earum doloribus ea doloremque quis&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;sint sit aut vero&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;porro aut necessitatibus eaque distinctio&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;repellendus veritatis molestias dicta incidunt&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;excepturi deleniti adipisci voluptatem et neque optio illum ad&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;sunt cum tempora&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;totam quia non&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;False&quot;,&quot;doloremque quibusdam asperiores libero corrupti illum qui omnis&quot;
&quot;2&quot;,&quot;Antonette&quot;,&quot;True&quot;,&quot;totam atque quo nesciunt&quot;
sylvain@ubuntu$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x15-api</code></li>
            <li>File: <code>1-export_to_CSV.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1733">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1733" data-batch-id="95" data-toggle="modal" data-target="#task-1733-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-1733-users-done-modal" data-task-id="1733" data-batch-id="95">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "1. Export to CSV"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm check-your-task-1733-modal-button" data-task-id="1733" data-toggle="modal" data-target="#task-test-correction-1733-correction-modal" id="task-num-1-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:1733}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1733-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "1. Export to CSV"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1733">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1733">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="1733">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1733}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1734" data-position="3" id="task-num-2">
      <div class="panel panel-default task-card " id="task-1734">
  <span id="user_id" data-id="306856"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      2. Export to JSON
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="306856"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>

<p>Requirements:</p>

<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: <code>{ &quot;USER_ID&quot;: [{&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}, {&quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS, &quot;username&quot;: &quot;USERNAME&quot;}, ... ]}</code></li>
<li>File name must be: <code>USER_ID.json</code></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ python3 2-export_to_JSON.py 2
sylvain@ubuntu$ cat 2.json
{&quot;2&quot;: [{&quot;task&quot;: &quot;suscipit repellat esse quibusdam voluptatem incidunt&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;distinctio vitae autem nihil ut molestias quo&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;et itaque necessitatibus maxime molestiae qui quas velit&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;adipisci non ad dicta qui amet quaerat doloribus ea&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;voluptas quo tenetur perspiciatis explicabo natus&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;aliquam aut quasi&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;veritatis pariatur delectus&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;nesciunt totam sit blanditiis sit&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;laborum aut in quam&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;repudiandae totam in est sint facere fuga&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;earum doloribus ea doloremque quis&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;sint sit aut vero&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;porro aut necessitatibus eaque distinctio&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;repellendus veritatis molestias dicta incidunt&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;excepturi deleniti adipisci voluptatem et neque optio illum ad&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;sunt cum tempora&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;totam quia non&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;doloremque quibusdam asperiores libero corrupti illum qui omnis&quot;, &quot;completed&quot;: false, &quot;username&quot;: &quot;Antonette&quot;}, {&quot;task&quot;: &quot;totam atque quo nesciunt&quot;, &quot;completed&quot;: true, &quot;username&quot;: &quot;Antonette&quot;}]}sylvain@ubuntu$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x15-api</code></li>
            <li>File: <code>2-export_to_JSON.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1734">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1734" data-batch-id="95" data-toggle="modal" data-target="#task-1734-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-1734-users-done-modal" data-task-id="1734" data-batch-id="95">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "2. Export to JSON"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm check-your-task-1734-modal-button" data-task-id="1734" data-toggle="modal" data-target="#task-test-correction-1734-correction-modal" id="task-num-2-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:1734}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1734-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "2. Export to JSON"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1734">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1734">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="1734">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1734}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>
    <div data-role="task1752" data-position="4" id="task-num-3">
      <div class="panel panel-default task-card " id="task-1752">
  <span id="user_id" data-id="306856"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      3. Dictionary of list of dictionaries
    </h3>

    <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="306856"></span>

    <!-- Progress vs Score -->

    <!-- Task Body -->
    <p>Using what you did in the task #0, extend your Python script to export data in the JSON format.</p>

<p>Requirements:</p>

<ul>
<li>Records all tasks from all employees</li>
<li>Format must be: <code>{ &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ], &quot;USER_ID&quot;: [ {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, {&quot;username&quot;: &quot;USERNAME&quot;, &quot;task&quot;: &quot;TASK_TITLE&quot;, &quot;completed&quot;: TASK_COMPLETED_STATUS}, ... ]}</code></li>
<li>File name must be: <code>todo_all_employees.json</code></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ python3 3-dictionary_of_list_of_dictionaries.py
sylvain@ubuntu$ cat todo_all_employees.json
{&quot;1&quot;: [{&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;delectus aut autem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;quis ut nam facilis et officia qui&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;fugiat veniam minus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;et porro tempora&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;laboriosam mollitia et enim quasi adipisci quia provident illum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;qui ullam ratione quibusdam voluptatem quia omnis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;illo expedita consequatur quia in&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;quo adipisci enim quam ut ab&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;molestiae perspiciatis ipsa&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;illo est ratione doloremque quia maiores aut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;vero rerum temporibus dolor&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;ipsa repellendus fugit nisi&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;et doloremque nulla&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;repellendus sunt dolores architecto voluptatum&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;ab voluptatum amet voluptas&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;accusamus eos facilis sint et aut voluptatem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;quo laboriosam deleniti aut qui&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;dolorum est consequatur ea mollitia in culpa&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;molestiae ipsa aut voluptatibus pariatur dolor nihil&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Bret&quot;, &quot;task&quot;: &quot;ullam nobis libero sapiente ad optio sint&quot;, &quot;completed&quot;: true}], &quot;2&quot;: [{&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;suscipit repellat esse quibusdam voluptatem incidunt&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;distinctio vitae autem nihil ut molestias quo&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;et itaque necessitatibus maxime molestiae qui quas velit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;adipisci non ad dicta qui amet quaerat doloribus ea&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;voluptas quo tenetur perspiciatis explicabo natus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;aliquam aut quasi&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;veritatis pariatur delectus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;nesciunt totam sit blanditiis sit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;laborum aut in quam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;repudiandae totam in est sint facere fuga&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;earum doloribus ea doloremque quis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;sint sit aut vero&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;porro aut necessitatibus eaque distinctio&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;repellendus veritatis molestias dicta incidunt&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;excepturi deleniti adipisci voluptatem et neque optio illum ad&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;sunt cum tempora&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;totam quia non&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;doloremque quibusdam asperiores libero corrupti illum qui omnis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Antonette&quot;, &quot;task&quot;: &quot;totam atque quo nesciunt&quot;, &quot;completed&quot;: true}], &quot;3&quot;: [{&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;aliquid amet impedit consequatur aspernatur placeat eaque fugiat suscipit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;rerum perferendis error quia ut eveniet&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;tempore ut sint quis recusandae&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;cum debitis quis accusamus doloremque ipsa natus sapiente omnis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;velit soluta adipisci molestias reiciendis harum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;vel voluptatem repellat nihil placeat corporis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;nam qui rerum fugiat accusamus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;sit reprehenderit omnis quia&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;ut necessitatibus aut maiores debitis officia blanditiis velit et&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;cupiditate necessitatibus ullam aut quis dolor voluptate&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;distinctio exercitationem ab doloribus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;nesciunt dolorum quis recusandae ad pariatur ratione&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;qui labore est occaecati recusandae aliquid quam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;quis et est ut voluptate quam dolor&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;voluptatum omnis minima qui occaecati provident nulla voluptatem ratione&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;deleniti ea temporibus enim&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;pariatur et magnam ea doloribus similique voluptatem rerum quia&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;est dicta totam qui explicabo doloribus qui dignissimos&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;perspiciatis velit id laborum placeat iusto et aliquam odio&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Samantha&quot;, &quot;task&quot;: &quot;et sequi qui architecto ut adipisci&quot;, &quot;completed&quot;: true}], &quot;4&quot;: [{&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;odit optio omnis qui sunt&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;et placeat et tempore aspernatur sint numquam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;doloremque aut dolores quidem fuga qui nulla&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;voluptas consequatur qui ut quia magnam nemo esse&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;fugiat pariatur ratione ut asperiores necessitatibus magni&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;rerum eum molestias autem voluptatum sit optio&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;quia voluptatibus voluptatem quos similique maiores repellat&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;aut id perspiciatis voluptatem iusto&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;doloribus sint dolorum ab adipisci itaque dignissimos aliquam suscipit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;ut sequi accusantium et mollitia delectus sunt&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;aut velit saepe ullam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;praesentium facilis facere quis harum voluptatibus voluptatem eum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;sint amet quia totam corporis qui exercitationem commodi&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;expedita tempore nobis eveniet laborum maiores&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;occaecati adipisci est possimus totam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;sequi dolorem sed&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;maiores aut nesciunt delectus exercitationem vel assumenda eligendi at&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;reiciendis est magnam amet nemo iste recusandae impedit quaerat&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;eum ipsa maxime ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Karianne&quot;, &quot;task&quot;: &quot;tempore molestias dolores rerum sequi voluptates ipsum consequatur&quot;, &quot;completed&quot;: true}], &quot;5&quot;: [{&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;suscipit qui totam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;voluptates eum voluptas et dicta&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;quidem at rerum quis ex aut sit quam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;sunt veritatis ut voluptate&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;et quia ad iste a&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;incidunt ut saepe autem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;laudantium quae eligendi consequatur quia et vero autem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;vitae aut excepturi laboriosam sint aliquam et et accusantium&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;sequi ut omnis et&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;molestiae nisi accusantium tenetur dolorem et&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;nulla quis consequatur saepe qui id expedita&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;in omnis laboriosam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;odio iure consequatur molestiae quibusdam necessitatibus quia sint&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;facilis modi saepe mollitia&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;vel nihil et molestiae iusto assumenda nemo quo ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;nobis suscipit ducimus enim asperiores voluptas&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;dolorum laboriosam eos qui iure aliquam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;debitis accusantium ut quo facilis nihil quis sapiente necessitatibus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;neque voluptates ratione&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Kamren&quot;, &quot;task&quot;: &quot;excepturi a et neque qui expedita vel voluptate&quot;, &quot;completed&quot;: false}], &quot;6&quot;: [{&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;explicabo enim cumque porro aperiam occaecati minima&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;sed ab consequatur&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;non sunt delectus illo nulla tenetur enim omnis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;excepturi non laudantium quo&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;totam quia dolorem et illum repellat voluptas optio&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;ad illo quis voluptatem temporibus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;praesentium facilis omnis laudantium fugit ad iusto nihil nesciunt&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;a eos eaque nihil et exercitationem incidunt delectus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;autem temporibus harum quisquam in culpa&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;aut aut ea corporis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;magni accusantium labore et id quis provident&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;consectetur impedit quisquam qui deserunt non rerum consequuntur eius&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;quia atque aliquam sunt impedit voluptatum rerum assumenda nisi&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;cupiditate quos possimus corporis quisquam exercitationem beatae&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;sed et ea eum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;ipsa dolores vel facilis ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;sequi quae est et qui qui eveniet asperiores&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;quia modi consequatur vero fugiat&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;corporis ducimus ea perspiciatis iste&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Leopoldo_Corkery&quot;, &quot;task&quot;: &quot;dolorem laboriosam vel voluptas et aliquam quasi&quot;, &quot;completed&quot;: false}], &quot;7&quot;: [{&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;inventore aut nihil minima laudantium hic qui omnis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;provident aut nobis culpa&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;esse et quis iste est earum aut impedit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui consectetur id&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;aut quasi autem iste tempore illum possimus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;ut asperiores perspiciatis veniam ipsum rerum saepe&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;voluptatem libero consectetur rerum ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;eius omnis est qui voluptatem autem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;rerum culpa quis harum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;nulla aliquid eveniet harum laborum libero alias ut unde&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui ea incidunt quis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui molestiae voluptatibus velit iure harum quisquam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;et labore eos enim rerum consequatur sunt&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;molestiae doloribus et laborum quod ea&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;facere ipsa nam eum voluptates reiciendis vero qui&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;asperiores illo tempora fuga sed ut quasi adipisci&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;qui sit non&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;placeat minima consequatur rem qui ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;consequatur doloribus id possimus voluptas a voluptatem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Elwyn.Skiles&quot;, &quot;task&quot;: &quot;aut consectetur in blanditiis deserunt quia sed laboriosam&quot;, &quot;completed&quot;: true}], &quot;8&quot;: [{&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;explicabo consectetur debitis voluptates quas quae culpa rerum non&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;maiores accusantium architecto necessitatibus reiciendis ea aut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;eum non recusandae cupiditate animi&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;ut eum exercitationem sint&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;beatae qui ullam incidunt voluptatem non nisi aliquam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;molestiae suscipit ratione nihil odio libero impedit vero totam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;eum itaque quod reprehenderit et facilis dolor autem ut&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;esse quas et quo quasi exercitationem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;animi voluptas quod perferendis est&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;eos amet tempore laudantium fugit a&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;accusamus adipisci dicta qui quo ea explicabo sed vero&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;odit eligendi recusandae doloremque cumque non&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;ea aperiam consequatur qui repellat eos&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;rerum non ex sapiente&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;voluptatem nobis consequatur et assumenda magnam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;nam quia quia nulla repellat assumenda quibusdam sit nobis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;dolorem veniam quisquam deserunt repellendus&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;debitis vitae delectus et harum accusamus aut deleniti a&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Maxime_Nienow&quot;, &quot;task&quot;: &quot;et praesentium aliquam est&quot;, &quot;completed&quot;: false}], &quot;9&quot;: [{&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;ex hic consequuntur earum omnis alias ut occaecati culpa&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;omnis laboriosam molestias animi sunt dolore&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;natus corrupti maxime laudantium et voluptatem laboriosam odit&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;reprehenderit quos aut aut consequatur est sed&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;fugiat perferendis sed aut quidem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;quos quo possimus suscipit minima ut&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;et quis minus quo a asperiores molestiae&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;recusandae quia qui sunt libero&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;ea odio perferendis officiis&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;quisquam aliquam quia doloribus aut&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;fugiat aut voluptatibus corrupti deleniti velit iste odio&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;et provident amet rerum consectetur et voluptatum&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;harum ad aperiam quis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;similique aut quo&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;laudantium eius officia perferendis provident perspiciatis asperiores&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;magni soluta corrupti ut maiores rem quidem&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;et placeat temporibus voluptas est tempora quos quibusdam&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;nesciunt itaque commodi tempore&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;omnis consequuntur cupiditate impedit itaque ipsam quo&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Delphine&quot;, &quot;task&quot;: &quot;debitis nisi et dolorem repellat et&quot;, &quot;completed&quot;: true}], &quot;10&quot;: [{&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;ut cupiditate sequi aliquam fuga maiores&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;inventore saepe cumque et aut illum enim&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;omnis nulla eum aliquam distinctio&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;molestias modi perferendis perspiciatis&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;voluptates dignissimos sed doloribus animi quaerat aut&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;explicabo odio est et&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;consequuntur animi possimus&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;vel non beatae est&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;culpa eius et voluptatem et&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;accusamus sint iusto et voluptatem exercitationem&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;temporibus atque distinctio omnis eius impedit tempore molestias pariatur&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;ut quas possimus exercitationem sint voluptates&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;rerum debitis voluptatem qui eveniet tempora distinctio a&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;sed ut vero sit molestiae&quot;, &quot;completed&quot;: false}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;rerum ex veniam mollitia voluptatibus pariatur&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;consequuntur aut ut fugit similique&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;dignissimos quo nobis earum saepe&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;quis eius est sint explicabo&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;numquam repellendus a magnam&quot;, &quot;completed&quot;: true}, {&quot;username&quot;: &quot;Moriah.Stanton&quot;, &quot;task&quot;: &quot;ipsam aperiam voluptates qui&quot;, &quot;completed&quot;: false}]}sylvain@ubuntu$
</code></pre>

  </div>

  <div class="list-group">
    <!-- Task URLs -->

    <!-- Github information -->
      <div class="list-group-item">
        <p><strong>Repo:</strong></p>
        <ul>
          <li>GitHub repository: <code>alx-system_engineering-devops</code></li>
            <li>Directory: <code>0x15-api</code></li>
            <li>File: <code>3-dictionary_of_list_of_dictionaries.py</code></li>
        </ul>
      </div>

    <!-- Self-paced manual review -->
  </div>

  <!-- Panel footer - Controls -->
  <div class="panel-footer">
      <div class="align-items-center d-flex justify-content-between">
        
<div>
    <button class="student_task_done btn btn-default btn-sm no" data-task-id="1752">
      <span class="no"><i aria-hidden="true" class="fa-regular fa-square "></i></span>
      <span class="yes"><i aria-hidden="true" class="fa-regular fa-square-check "></i></span>
      <span class="pending"><i aria-hidden="true" class="fa-solid fa-spinner  fa-spin-pulse"></i></span>
      Done<span class="no pending">?</span><span class="yes">!</span>
    </button>

  <button class="student-task-done-by btn btn-default btn-sm" data-task-id="1752" data-batch-id="95" data-toggle="modal" data-target="#task-1752-users-done-modal">
    Help
  </button>
  <div class="modal fade users-done-modal" id="task-1752-users-done-modal" data-task-id="1752" data-batch-id="95">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title">Learners who are done with "3. Dictionary of list of dictionaries"</h4>
        </div>
        <div class="modal-body">
            <div class="list-group">
            </div>
            <div class="spinner">
                <div class="bounce1"></div>
                <div class="bounce2"></div>
                <div class="bounce3"></div>
            </div>
            <div class="error"></div>
        </div>
        </div>
    </div>
</div>


      <button class="btn btn-default btn-sm check-your-task-1752-modal-button" data-task-id="1752" data-toggle="modal" data-target="#task-test-correction-1752-correction-modal" id="task-num-3-check-code-btn" data-gtm-custom-event-name="task_checker_modal" data-gtm-custom-event-options='{&quot;taskId&quot;:1752}'>
          Check your code
      </button>
      <div class="modal fade task_correction_modal student_modal" id="task-test-correction-1752-correction-modal">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                <h4 class="modal-title">Correction of "3. Dictionary of list of dictionaries"</h4>
            </div>
            <div class="modal-body">
                <div class="actions">
                    <center>
                        <div class="alert alert-info hidden"></div>

                        <button name="button" type="submit" class="btn btn-primary correction_request_test_send" data-task-id="1752">Start a new test</button>
                        <button class="btn btn-default close-modal hidden" data-dismiss="modal" type="button">Close</button>

                        <div class="spinner" style="display: none;">
                            <div class="bounce1"></div>
                            <div class="bounce2"></div>
                            <div class="bounce3"></div>
                        </div>
                        <div class="error"></div>
                        <div class="info"></div>
                    </center>
                </div>
                <div class="result"></div>

                <div class="help">
    <button data-task-id="1752">
        <i aria-hidden="true" class="fa-solid fa-circle-info "></i>
    </button>
    <div class="help-container" data-task-id="1752">
        <div class="check-line">
            <div class="check-inline requirement success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Requirement success
            </div>
            <div class="check-inline requirement fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Requirement fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline code success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Code success
            </div>
            <div class="check-inline code fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Code fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline efficiency success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Efficiency success
            </div>
            <div class="check-inline efficiency fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Efficiency fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline answer success">
                <i aria-hidden="true" class="fa-solid fa-circle-check "></i>
                Text answer success
            </div>
            <div class="check-inline answer fail">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Text answer fail
            </div>
        </div>
        <div class="check-line">
            <div class="check-inline requirement fail offline">
                <i aria-hidden="true" class="fa-solid fa-circle-xmark "></i>
                Skipped - Previous check failed
            </div>
        </div>
    </div>
</div>

            </div>
        </div>
    </div>
</div>



    <button class="btn btn-default btn-sm" data-toggle="modal" data-target="#container-specs-modal" data-gtm-custom-event-name="task_sandbox_modal" data-gtm-custom-event-options="{&quot;taskId&quot;:1752}"><i aria-hidden="true" class="fa-solid fa-terminal "></i><span>Get a sandbox</span></button>

</div>


        <div class="fs-4">
        </div>
      </div>


  </div>
</div>

    </div>





          <div class="modal fade" id="container-specs-modal"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button><h4 class="modal-title">Recommended Sandbox</h4></div><div class="modal-body"><div data-react-class="user_containers/ContainerSpecs" data-react-props="{&quot;containerModelName&quot;:&quot;Sandbox&quot;,&quot;containerSpecs&quot;:[{&quot;available&quot;:true,&quot;description&quot;:&quot;\u003cp\u003eBasic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Foundations\u003c/p\u003e\n&quot;,&quot;id&quot;:39,&quot;name&quot;:&quot;Ubuntu 20.04&quot;,&quot;online&quot;:true,&quot;container&quot;:{&quot;container_id&quot;:null,&quot;id&quot;:615351,&quot;restart_uri&quot;:&quot;/user_containers/615351/restart.json&quot;,&quot;status&quot;:&quot;asleep&quot;,&quot;uri&quot;:&quot;/user_containers/615351.json&quot;,&quot;wake_uri&quot;:&quot;/user_containers/615351/wake.json&quot;,&quot;webterm_uri&quot;:&quot;/user_containers/615351/webterm&quot;,&quot;host&quot;:null,&quot;password&quot;:&quot;571368dfba4b55e3449f&quot;,&quot;ports&quot;:{&quot;8080&quot;:55756,&quot;22&quot;:55765,&quot;3000&quot;:55762,&quot;3306&quot;:55761,&quot;443&quot;:55763,&quot;5001&quot;:55758,&quot;80&quot;:55764,&quot;4000&quot;:55760,&quot;5000&quot;:55759,&quot;8000&quot;:55757}}}],&quot;containersLimit&quot;:2,&quot;csrfToken&quot;:&quot;4EJC0xv9RUkd6CjhDbAXhW6Yo7zkKAERWwUjeyqD-MSXUK_jAVMOX9mZlXnpXGVBSQGRZtUFOtr16wTuCsbABA&quot;,&quot;startStatusURI&quot;:&quot;/user_containers/start_status.json&quot;,&quot;startURI&quot;:&quot;/user_containers/start.json&quot;}" data-react-cache-id="user_containers/ContainerSpecs-0"></div></div></div></div></div>

  </div>
</div>


      </article>

      <div class="copyright">Copyright © 2024 ALX, All rights reserved.</div>

    </main>

        <button class="btn btn-primary atop-zendesk" id="search-button" data-search-active="false" data-toggle="modal" data-target="#search-modal">
  <i aria-hidden="true" class="fa-solid fa-magnifying-glass "></i>
  <i aria-hidden="true" class="fa-solid fa-window-minimize "></i>
</button>

        <div class="modal fade" id="search-modal" tabindex="-1" role="dialog" aria-labelledby="search-modal-label">
    <div class="modal-dialog modal-md">
        <div class="modal-content">
            <div class="modal-header">
                <div id="search-bar-container">
    <input id="search-bar"
            autocomplete="off"
            type="text"
            name="hbtn-search-bar"
            placeholder="✨Start search by typing in this field✨">
</div>

            </div>
            <div class="modal-body">
                <div id="modal-spinner" class="spinner gap">
                    <div class="bounce1"></div>
                    <div class="bounce2"></div>
                    <div class="bounce3"></div>
                </div>
                <div id="search-results-container">
</div>

            </div>
        </div>
    </div>
</div>



        <div class="modal fade" id="markdownGuideModal" tabindex="-1" role="dialog" aria-labelledby="markdownGuideModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-md">
    <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">Markdown Guide</h4>
        </div>
        <div class="modal-body">
            <h4>Emphasis</h4>
<pre>**<strong>bold</strong>**
*<em>italics</em>*
~~<strike>strikethrough</strike>~~</pre>
<h4>Headers</h4>
<pre># Big header
## Medium header
### Small header
#### Tiny header</pre>
<h4>Lists</h4>
<pre>* Generic list item
* Generic list item
* Generic list item

1. Numbered list item
2. Numbered list item
3. Numbered list item</pre>
<h4>Links</h4>
<pre>[Text to display](http://www.example.com)</pre>
<h4>Quotes</h4>
<pre>> This is a quote.
> It can span multiple lines!</pre>
<h4>Images</h4>
<p>CSS style available: <code>width, height, opacity</code></p>
<pre>![](http://www.example.com/image.jpg)
![](http://www.example.com/image.jpg | width: 200px)
![](http://www.example.com/image.jpg | height: 124px | width: 80px | opacity: 0.6)
</pre>
<h4>Tables</h4>
<pre>| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John     | Doe      | Male     |
| Mary     | Smith    | Female   |

<em>Or without aligning the columns...</em>

| Column 1 | Column 2 | Column 3 |
| -------- | -------- | -------- |
| John | Doe | Male |
| Mary | Smith | Female |
</pre>
<h4>Displaying code</h4>
<pre>`var example = "hello!";`

<em>Or spanning multiple lines...</em>

```
var example = "hello!";
alert(example);
```</pre>
        </div>
    </div>
  </div>
</div>


        <script id="ze-snippet" src="https://static.zdassets.com/ekr/snippet.js?key=0e932b79-b1e7-49d4-88a9-75d1fc357a07"></script>
        <script type="text/javascript">
          zE('webWidget', 'prefill', {
              email: {
                  value: 'kabanda.patrick2580@gmail.com',
                  readOnly: true
              }
          });
        </script>
  </body>
</html>
