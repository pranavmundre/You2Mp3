
const cacheName = 'You2MP3';
const staticAssets = [
	'/',
]

self.addEventListener('install', async e =>{
	const cache = await caches.open(cacheName);
	await cache.addAll(staticAssets);
	return self.skipWaiting();
});

self.addEventListener('activate', async e =>{
	self.clients.claim();
});

// self.addEventListener('fetch', async e =>{
// 	const req = e.request;
// 	const url = new URL(req.url);

// 	if (url.origin == location.origin) {
// 		e.respondWith(cacheFirst(req));
// 	}
// 	else{
// 		e.respondWith(networkkAndCache(req));
// 	}
// });

self.addEventListener('fetch', function(event) {
const promiseChain = doSomethingAsync()
      .then(() => doSomethingAsyncThatReturnsAURL(event))
      .then(someUrl => fetch(someUrl));
event.respondWith(promiseChain);
});
