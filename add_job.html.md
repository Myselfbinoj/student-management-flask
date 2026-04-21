

{% extends "base.html" %}

{% block content %}

<h2>Add Job</h2>

<form method="POST">

&nbsp;   <input name="company" class="form-control mb-2" placeholder="Company" required>

&nbsp;   <input name="role" class="form-control mb-2" placeholder="Role" required>

&nbsp;   <select name="status" class="form-control mb-2">

&nbsp;       <option>Applied</option>

&nbsp;       <option>Interview</option>

&nbsp;       <option>Rejected</option>

&nbsp;       <option>Offer</option>

&nbsp;   </select>

&nbsp;   <textarea name="notes" class="form-control mb-2" placeholder="Notes"></textarea>

&nbsp;   <button class="btn btn-primary">Save</button>

</form>

{% endblock %}

