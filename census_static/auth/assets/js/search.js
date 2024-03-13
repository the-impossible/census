const searchField = document.getElementById('searchField')
const fromAjaxSearch = document.getElementById('fromAjaxSearch')
const fromIndexSearch = document.getElementById('fromIndexSearch')
const fromCategory = document.getElementById('fromCategory')
const count = document.getElementById('count')
const fromAjax = document.getElementById('fromAjax')

searchField.addEventListener('keyup', (e) => {
    const searchVal = e.target.value

    let url = ''

    if (searchVal.trim().length > 0 ) {
        fetch(url, {
            body:   JSON.stringify({'searchText':searchVal}),
            method: 'POST',
            headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
            }
        })
        .then((res) => res.json())
        .then((data) => {
			fromAjax.innerHTML = ''
			data.forEach((element) => {
				if (data.length === 0){
					fromCategory.style.display = 'block'
					fromIndexSearch.style.display = 'block'
				}else{
					fromCategory.style.display = 'none'
					fromIndexSearch.style.display = 'none'
					fromAjax.innerHTML += 
						`
							<div class="col-lg-6">												  
									<div class="single-job mb-4 d-lg-flex justify-content-between">
											<div class="job-text">
													<h4 class="">${element.title}</h4>
													<ul class="mt-4">
															<li class="mb-3"><h5><i class="fa fa-map-marker"></i> ${element.location__name} </h5></li>
															<li class="mb-3"><h5><i class="fa fa-pie-chart"></i> ${ element.category__name }</h5></li>
															<li><h5><i class="fa fa-clock-o"></i> ${ element.deadline }</h5></li>
													</ul>
											</div>
											<div class="job-btn align-self-center">
													<a href="/home_job_details/${element.id}" class="third-btn">More</a>
											</div>
									</div>
							</div>
						`
				}
			})
			count.innerHTML = data.length
        })
    }
})